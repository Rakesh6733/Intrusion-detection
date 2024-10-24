from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

class U(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=264, unique=True)
    password = models.CharField(max_length=128, default='')
    cpass = models.CharField(max_length=64,default='')
    phone_number = PhoneNumberField()
    dob = models.DateField(default=timezone.now)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    social = models.URLField(max_length=1000, null=True, blank=True)
    

class Job_details(models.Model):

    TYPE = (
        ('FULL TIME', 'FULL TIME'),
        ('PART TIME', 'PART TIME')
    )

    jobname = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
    Type = models.CharField(max_length=30, choices=TYPE)
    duration = models.DateField(default=timezone.now)
    salary = models.IntegerField()
    link = models.URLField(max_length=1000)

    def __str__(self):
        return self.jobname
    
class Alumni(models.Model):

    Years = (
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
    )

    grad = (
        ('2022', '2022'),
        ('2021', '2021'),
        ('2020', '2020'),
        ('2019', '2019'),
        ('2018', '2018'),
        ('2017', '2017'),
        ('2016', '2016'),
        ('2015', '2015'),
    )

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    Faculty = (
        ('Faculty of Science', 'Faculty of Science'),
        ('Faculty of Engineering', 'Faculty of Engineering'),
        ('Faculty of Arts And Law','Faculty of Arts And Law'),
        ('Faculty of Management','Faculty of Management'),
        ('Faculty of Design','Faculty of Design'),
    )

    user = models.OneToOneField(U, on_delete=models.CASCADE, default="user")
    joining_year = models.CharField(choices=Years, max_length=4)
    grad_year = models.CharField(choices=grad, max_length=4)
    Degree = models.CharField(max_length=100)
    Reg_no = models.IntegerField(primary_key=True, default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    jobtitle = models.CharField(max_length=50)
    address = models.CharField(max_length=200, null=True, blank=True)
    faculty_stream = models.CharField(max_length=50, choices=Faculty, default='Faculty of Engineering')
    

    def __str__(self):
        return str(self.Reg_no)
    

class Contact(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=100, primary_key=True)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.email
    

class Gallery(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=1000, blank=True, null=True)
    upload = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateField(default=timezone.now)
    name = models.CharField(max_length=30)
    url = models.URLField(max_length=1000, blank=True, null=True)
    upload = models.ImageField(upload_to='images/', blank=True, null=True)
    content = models.TextField(max_length=1000,)

    def __str__(self):
        return self.title
    


class Profile(models.Model):
    # Here it is linked to user table
    # Get the instance from the profile table by using get i.e Profile.objects.get(user=user_id)
    # now you can access the user table by using this instance like Profile.user.email
    user = models.OneToOneField(U,primary_key=True, verbose_name="User", on_delete=models.CASCADE)
    
    # create an default.jpg pic to render, if not user is selected the image
    image = models.ImageField(default="default.jpg", upload_to = "Reg/images")

    def __str__(self):
        return f'{self.user.fname} Profile'
