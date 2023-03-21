from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Project, TODO
from usersapp.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)
    # users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['projectname', 'projectlink', 'users']


class TODOModelSerializer(ModelSerializer):
    create_user = UserModelSerializer()
    project = ProjectModelSerializer()

    class Meta:
        model = TODO
        fields = ['project', 'todo_text', 'create_date', 'create_user', 'change_date', 'status']
