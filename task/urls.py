"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user.views import Create, ShowGroups, ShowPermissions, ShowUsers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', Create.as_view(), name='create'),
    path('show-user/<str:username>', ShowUsers.as_view(), name='show_user'),
    path('show-group/<str:username>', ShowGroups.as_view(), name='show_group'),
    path('show-permissions/<str:username>', ShowPermissions.as_view(), name='show_permission'),
]
