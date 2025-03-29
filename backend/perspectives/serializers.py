from rest_framework import serializers
from .models import Perspective

class PerspectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perspective
        fields = ['user', 'project', 'subject', 'category', 'text', 'created_at', 'updated_at']
        read_only_fields = ['project', 'created_at', 'updated_at']