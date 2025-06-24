from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        label='First name*',
        help_text='',
        widget=forms.TextInput(attrs={'placeholder': 'First name*'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        label='Last name*',
        help_text='',
        widget=forms.TextInput(attrs={'placeholder': 'Last name*'})
    )
    email = forms.EmailField(
        max_length=254, 
        required=False, 
        label='Email address',
        help_text='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email address'})
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        labels = {
            'username': 'Username*',
            'password1': 'Password*',
            'password2': 'Confirm password*',
        }
