from django.db import models

# Create your models here.
from django.db import models


class Permission(models.Model):
    name_per = models.CharField(max_length=20)
    group_permission = models.BooleanField(default=False, null=True, blank=False)
    users_permission = models.BooleanField(default=False, null=True, blank=False)
    rules_permission = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return f'{self.name_per}'


class Group(models.Model):
    name = models.CharField(max_length=20)
    permission = models.ForeignKey(Permission, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} / Permission : {self.permission.name_per}'


class User(models.Model):
    username = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.username} --> {self.group.name} : {self.group.permission}'
