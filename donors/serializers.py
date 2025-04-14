from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['id','username','email']

class DonorProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = DonorProfile
        fields = '__all__'

class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUpdate
        fields = '__all__'

