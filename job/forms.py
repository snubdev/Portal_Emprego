from django import forms
from .models import Job_Registration

class Job_RegistraionForm(forms.ModelForm):
    class Meta:
        model = Job_Registration
        fiels = ['name', 'email', 'phone', 'curriculum']

