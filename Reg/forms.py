from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import U

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = U
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = U
        fields = ("username", "email")