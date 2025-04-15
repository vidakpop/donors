from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('project-updates', ProjectUpdateViewSet)

