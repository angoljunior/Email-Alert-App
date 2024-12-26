from django.shortcuts  import render,redirect
from .forms import JobAlertSubscriptionForm
from django.http import HttpResponse
from .models import JobAlertSubscription
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User


#Create views here
def login_user(request):
    if request.method =='POST':
        username    = request.POST['username']
        email       = request.POST['email']
        password    = request.POST['password']
         
        user = authenticate(username=username,password=password,email=email)

        if user is not None:
            login(request ,user)
            messages.success(request , "Login succesfull")
            return redirect('subscribe_job_alerts')

        else:
            messages.success(request , "There was an error trying to log in, Try Again!")
            return redirect('login-user')
    
    else:
        return render(request,'login.html' , {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You have been logged out...Thanks for using our service"))
	return redirect('subscribe_job_alerts')



def subscribe_to_job_alerts(request):
    if request.method == 'POST':
        # Get the values from the POST request
        job_name = request.POST.get('job_name')  # Replace with actual field name in your form
        job_location = request.POST.get('job_location')  # Replace with actual field name in your form
        
        # Ensure all fields are provided
        if not job_name or not job_location:
            message = "Both job name and job location are required."
            return render(request, 'job_alert.html', {'message': message})
        
        # Create and save the JobAlertSubscription instance
        subscription = JobAlertSubscription(
            keyword=job_name,
            location=job_location,
            user=request.user  # Ensure the user is logged in
        )
        subscription.save()
        
        # Return success message
        #message = "New Alert Created successfully. You will automatically receive an email when new job posts arrive."
        messages.success(request,"New Alert Created successfully. You will automatically receive an email when new job posts arrive")
        return redirect('subscribe_job_alerts') 
    else:
        # Render the form for a GET request
        return render(request, 'job_alert.html', {})
