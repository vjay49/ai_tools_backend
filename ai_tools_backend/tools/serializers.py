from rest_framework import serializers
from .models import Tool

class ToolSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Tool
        fields = '__all__'
