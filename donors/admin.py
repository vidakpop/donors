from django.contrib import admin
from .models import DonorProfile, Project, ProjectUpdate, Donation, Notification


admin.site.register(DonorProfile)
admin.site.register(Project)
admin.site.register(ProjectUpdate)
admin.site.register(Donation)
admin.site.register(Notification)