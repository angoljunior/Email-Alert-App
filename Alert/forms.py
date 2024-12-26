from django import forms
from .models import JobAlertSubscription

class JobAlertSubscriptionForm(forms.ModelForm):
    keyword    = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'contact__input', 'placeholder':'Phone'}), required=True)
    location   = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'contact__input', 'placeholder':'location'}), required=True)

    class Meta:
        model = JobAlertSubscription
        fields = ['keyword', 'location']
