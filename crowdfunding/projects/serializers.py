from rest_framework import serializers
from .models import Project, Pledge
from datetime import datetime, timedelta
from django.utils import timezone



class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    # supporter = serializers.CharField(max_length=200)
    supporter_id = serializers.IntegerField()
    project_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class PledgeDetailSerializer(PledgeSerializer):

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment',instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.supporter_id = validated_data.get('supporter_id',instance.supporter_id)

        instance.save()
        return instance

class ProjectSerializer(serializers.Serializer):
    # Using current time 
    # Calculating future dates for 1 month 
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    # is_open = serializers.BooleanField()
    is_open = serializers.SerializerMethodField()
    date_created = serializers.DateTimeField(default=datetime.now())
    date_end = serializers.DateTimeField(default = datetime.now() + timedelta(days = 30) )
    # owner = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source='owner.id')
    # pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def get_is_open(self, obj):
            if datetime.now() > obj.date_end:
                is_open = False
            else:
                is_open = True
            return is_open

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    def delete(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    # def get_is_open(self, obj):
    #     project = self.get_object(pk=pk)
    #     if datetime.now > obj.project.date_end:
    #         is_open = False
    #     else:
    #         is_open = True
    #     return is_open
