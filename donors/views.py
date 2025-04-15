from django.shortcuts import render
from rest_framework import viewsets,generics,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Donor >> Project listing and details
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

#NGO >> Create and Edit Project
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save()

    # def perform_update(self, serializer):
    #     serializer.save()

class ProjectUpdateViewSet(viewsets.ModelViewSet):
    queryset = ProjectUpdate.objects.all()
    serializer_class = ProjectUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save()

    # def perform_update(self, serializer):
    #     serializer.save()

# Donor >> Profile view and Update
class DonorProfileView(APIView):
    permissions_classes = [permissions.IsAuthenticated]


