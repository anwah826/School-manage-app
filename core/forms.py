from django import forms
from django.contrib.auth.models import User
from .models import Profile, SupportMessage



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)


    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role','phone','student_id','date_of_birth']

class SupportForm(forms.ModelForm):
    class Meta:
        model = SupportMessage
        fields = ['subject', 'message']