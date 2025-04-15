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

    def get(self, request):
        profile, created = DonorProfile.objects.get_or_create(user=request.user)
        return Response(DonorProfileSerializer(profile,created).data)
    
    def put(self, request):
        profile = DonorProfile.objects.get(user=request.user)
        serializer = DonorProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Donor >> Donation hsistory
class AllDonationsView(generics.ListAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

# Donor >> Create Donation (simulate payment)
class DonationCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data=request.data
        donation = Donation.obkjects.create(
            donor=request.user,
            project_id=data['project'],
            amount=data['amount'],
            payment_reference=data['payment_reference','TINA123456']
        )
        return Response(DonationSerializer(donation).data,status=status.HTTP_201_CREATED)
    
# Donor >> Notifications
class DonorNotificationsView(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

