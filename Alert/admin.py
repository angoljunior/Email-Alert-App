from django.contrib import admin
from .models import JobAlertSubscription,JobPost

# Register your models here.
admin.site.register(JobPost)
admin.site.register(JobAlertSubscription)