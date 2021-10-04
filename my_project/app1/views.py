from django.shortcuts import render

# REST Framework
from rest_framework import viewsets
from .serializers import TodoSerializer
from app1 import views
from .models import Todo


# Create your views here.
def home_view(request):
    return render(request, "index.html")


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()