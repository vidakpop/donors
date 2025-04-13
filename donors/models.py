from django.db import models
from django.contrib.auth.models import User

class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
