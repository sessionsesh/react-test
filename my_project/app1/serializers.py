from rest_framework import serializers
from .models import Todo


# This code specifies the model to work with and the fields to be converted to JSON
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
