"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app1 import views

# FOR LAMBDA
from django.shortcuts import render

# REST
from rest_framework import routers
from django.urls import include
router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view),
    path('', lambda request: render(request, 'kirill.html')),
    path('api/', include(router.urls))
]