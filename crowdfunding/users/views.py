from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from .permissionsUser import IsUserOrReadOnly
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserDetailSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user = account).key
            data["email"] = account.email
            data["token"] = token
            return Response(serializer.data)
            # return Response(data)
        return Response(serializer.errors)

class CustomUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsUserOrReadOnly]
    def get_object(self, pk):
        try:
            # return CustomUser.objects.get(pk=pk)
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
        

    def put(self, request, pk):
    # it is for update 
        users = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(instance=users, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'user_full_name': user.full_name,
        })