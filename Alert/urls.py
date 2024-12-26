from django.urls import path
from .views import subscribe_to_job_alerts,login_user,logout_user

urlpatterns = [
    path('subscribe/', subscribe_to_job_alerts, name='subscribe_job_alerts'),
    path('login/' ,login_user ,name='login-user'),
    path('logout/', logout_user , name='logout_user'),
]
