from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('project-updates', ProjectUpdateViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Donor endpoints
    path('donor/projects/', ProjectListView.as_view()),
    path('donor/project/<int:pk>/', ProjectDetailView.as_view()),
    path('donor/profile/', DonorProfileView.as_view()),
    path('donor/donations/', DonorDonationHistoryView.as_view()),
    path('donor/donate/', DonationCreateView.as_view()),
    path('donor/notifications/', DonorNotificationsView.as_view()),
    path('donor/notification/read/<int:pk>/', MarkNotificationReadView.as_view()),

    # NGO endpoints
    path('ngo/donations/', AllDonationsView.as_view()),
    path('ngo/donation-notifications/', NewDonationNotificationsView.as_view()),
]