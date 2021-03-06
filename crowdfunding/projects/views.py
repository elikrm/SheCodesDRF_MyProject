from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer,ProjectDetailSerializer,PledgeDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

class ProjectList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        # return Response(serializer.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
            )
        return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project

        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        # serializer = ProjectSerializer(project)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        # it is for update 
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(instance=project, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# this class is showing the project progress
class ProjectProgress(APIView):
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project

        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        # return Response(serializer.data)
        progress_pledge = serializer.data
        # return Response(progress_pledge["pledges"])
        
        print_progress = {}
        print_progress["amount_progress"] = 0
        for i in range(len(progress_pledge["pledges"])):
            print_progress["amount_progress"] += progress_pledge["pledges"][i]["amount"]
        return Response(print_progress)

class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
            )
        return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetailList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsSupporterOrReadOnly]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge

        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        # serializer = ProjectSerializer(project)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        # it is for update 
        pledge = self.get_object(pk)
        data = request.data
        serializer = PledgeDetailSerializer(instance=pledge, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


