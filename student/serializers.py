from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', required=False)
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name', allow_null=True, allow_blank=True)
    email = serializers.CharField(source='user.email', required=False)
    password = serializers.CharField(source='user.password', required=False)
    is_active = serializers.BooleanField(source='user.is_active', read_only=True)

    class Meta:
        model = Student
        fields = '__all__'