from django.db import models
from usersapp.models import User


class Project(models.Model):
    projectname = models.CharField(max_length=64, unique=True)
    projectlink = models.CharField(max_length=64)
    users = models.ManyToManyField(User)


class TODO(models.Model):
    create_user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=256)
    create_date = models.DateField()
    change_date = models.DateField()
    status = models.PositiveIntegerField()
