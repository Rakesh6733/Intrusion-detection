from django.contrib import admin
from .models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .forms import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = U
    list_display = ["email", "username",]


class UAdmin(admin.ModelAdmin):
    list_display = ('id', 'fname', 'lname', 'email', 'cpass', 'phone_number', 'img', 'social')

class Job_detailsAdmin(admin.ModelAdmin):
    list_display = ('jobname', 'desc', 'Type', 'duration', 'salary', 'link')

admin.site.register(U, CustomUserAdmin)
admin.site.unregister(Group)
admin.site.register(Job_details)
admin.site.register(Alumni)
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(News)
admin.site.register(Profile)