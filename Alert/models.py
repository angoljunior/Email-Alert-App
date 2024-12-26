from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import User


#Create models here
class JobPost(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    location    = models.CharField(max_length=100)
    # Other job fields

    def __str__(self):
        return self.title

class JobAlertSubscription(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword     = models.CharField(max_length=100, blank=True,null=True)  # E.g., 'Software Developer'
    location    = models.CharField(max_length=100, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.keyword}"

@receiver(post_save, sender=JobPost)
def send_job_alert_email(sender, instance, created, **kwargs):
    if created:  # Only send an email for new job posts
        subscribers = JobAlertSubscription.objects.filter(
            keyword__icontains=instance.title
        )
        
        for subscription in subscribers:
            send_mail(
                subject=f"New Job Alert: {instance.title}",
                message=f"A new job '{instance.title}' has been posted in {instance.location}. Check it out!",
                from_email="nanakofi@gmail.com",  # Replace with your email
                recipient_list=[subscription.user.email],
                fail_silently=False,
            )


