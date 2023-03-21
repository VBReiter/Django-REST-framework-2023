from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer
# from usersapp.models import User
# from usersapp.serializers import UserModelSerializer
#
# def user_get(request, pk=None):
#     if pk is not None:
#         user = User.objects.get(pk=pk)
#         serializer = UserModelSerializer(user)
#     else:
#         users = User.objects.all()
#         serializer = UserModelSerializer(users, many=True)
#
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data)


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer


