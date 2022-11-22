from django import forms
from .models import Job_Registration, Job_Profile
from django.contrib.auth.models import User


class Job_RegistraionForm(forms.ModelForm):
    class Meta:
        model = Job_Registration
        fields = ('name', 'email', 'phone', 'curriculum')


class SearchForm(forms.Form):
    query = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('A senha não corresponde')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class Job_ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Job_Profile
        fields = ('date_of_birth',)
