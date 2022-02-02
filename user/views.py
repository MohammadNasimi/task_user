from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from .models import User, Group, Permission

from django.urls import reverse_lazy


class Create(generic.CreateView):
    model = User
    template_name = 'create.html'
    fields = "__all__"
    success_url = reverse_lazy('create')


class ShowUsers(View):
    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        user = User.objects.get(username=username)
        if user.group.permission.users_permission:
            users = User.objects.all()
            return render(request, 'ShowUsers.html', context={'users': users})
        else:
            return HttpResponse('no permission to see users', status=404)


class ShowGroups(View):
    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        user = User.objects.get(username=username)
        if user.group.permission.group_permission:
            groups = Group.objects.all()
            return render(request, 'ShowGroups.html', context={'groups': groups})
        else:
            return HttpResponse('no permission to see groups', status=404)


class ShowPermissions(View):
    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        user = User.objects.get(username=username)
        if user.group.permission.rules_permission:
            permissions = Permission.objects.all()
            return render(request, 'ShowPermissions.html', context={'permissions': permissions})
        else:
            return HttpResponse('u have no permission to see permissions', status=404)
