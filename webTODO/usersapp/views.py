from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse

from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


def user_get(request, pk=None):
    if pk is not None:
        user = User.objects.get(pk=pk)
        serializer = UserModelSerializer(user)
    else:
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)
