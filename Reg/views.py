from pyexpat.errors import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import RegexValidator
from .models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django import forms
# Create your views here.

ML = [
    ('1', 'Single'),
    ('2', 'Married')
]

class NewTaskForm(forms.Form):

    fname = forms.CharField(max_length=32,help_text="First Name", widget=forms.TextInput(attrs={
        "class":"form-control",
        'aria-label':'Name',
    }))

    lname = forms.CharField(max_length=32,help_text="First Name", widget=forms.TextInput(attrs={
        "class":"form-control",
        'aria-label':'Name',
    }))

    Email = forms.EmailField(max_length=264, widget=forms.EmailInput(attrs={
        'class':'form-control'
    }))

    phoneno = PhoneNumberField()

    y_o_p =  forms.CharField(max_length=4)

    d_o_b = forms.DateField(required=True, widget=forms.DateInput(attrs={
        'class':'form-control'
    }))

    marry = forms.ChoiceField(widget=forms.RadioSelect, choices=ML)

    Profession = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
    }))

    address = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':'10',
        'cols':'50',
        'aria-label':'Address'
    }))

    city = forms.CharField(max_length="30", help_text='City')
    state = forms.CharField(max_length="30", help_text='State')
    pincode = forms.CharField(max_length=4, validators=[RegexValidator(r'^\d{4}$', 'PIN must be a 4-digit number.')])
    life = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':'4',
        'cols':'8',
        'aria-label':'Life after graduation'
    }))
    memories = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class':'form-control',
        'rows':'4',
        'cols':'8',
        'aria-label':'Memories'
    }))
    




def about(request):
    return render(request, 'Reg/about.html')

def news(request):
    news = News.objects.all()
    return render(request, 'Reg/news.html', {
        'news': news,
    })

def gallery(request):

    photos = Gallery.objects.all()
    return render(request, 'Reg/gallery.html',{
        'photos':photos,

    })

def alumni(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        cpass = request.POST['cpass']
        faculty_stream = request.POST['faculty_stream']
        joining_year = request.POST['joining_year']
        grad_year = request.POST['grad_year']
        Degree = request.POST['Degree']
        Reg_no = request.POST['Reg_no']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        jobtitle = request.POST['jobtitle']
        address = request.POST['address']

        us = U(
            fname=fname,
            lname=lname,
            email=email,
            cpass=cpass,
            phone_number=phone_number,
        )

        us.save()
        
        alumni_1 = Alumni(
            user = us,
            joining_year=joining_year,
            grad_year=grad_year,
            Degree=Degree,
            Reg_no=Reg_no,
            gender=gender,
            jobtitle=jobtitle,
            address=address,
            faculty_stream=faculty_stream,
        )

        
        
        alumni_1.save()
        

        
        alumnis = Alumni.objects.all()
        
        return render(request, 'Reg/alumni.html',{
            'alumnis':alumnis,
            

        })



    alumnis = Alumni.objects.all()

    return render(request, 'Reg/alumni.html',{
        'alumnis':alumnis
    })

def contact(request):

    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(
            firstName = firstName,
            lastName = lastName,
            email = email,
            message = message
        )

        contact.save()

    return render(request, 'Reg/contact.html')

def login_view(request):
    if request.method == "POST":

        # accessing the form data
        email = request.POST['email']
        password = request.POST['password']

        # check if username and password are correct, returning user object
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request,'Invalid email or password')
    return render(request, 'Reg/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('home')

def jobs(request):

    if request.method == "POST":
            jobname = request.POST['jobname']
            desc = request.POST['desc']
            Type = request.POST['Type']
            duration = request.POST['duration']
            salary = request.POST['salary']
            link = request.POST['link']

            j = Job_details(
                jobname = jobname,
                desc = desc,
                Type = Type,
                duration = duration,
                salary = salary, 
                link = link
            )
            j.save()

            jobs = Job_details.objects.all()

            return render(request, 'Reg/jobs.html', {
                
                'jobs':jobs,
            })
    jobs = Job_details.objects.all()
    return render(request, 'Reg/jobs.html', {
        'jobs':jobs
    })



def jobform(request):
    return render(request, 'Reg/jobform.html')

def home(request):
    #if user is authenticated then render the user image 
    
    return render(request, 'Reg/index.html' )

def reg(request):
    return render(request, 'Reg/Registration.html')

def form(request):
    
    form = UserCreationForm()

    if request.method=="POST":

        # get info from the form
        form = UserCreationForm(request.POST)

        


    return render(request, 'Reg/form.html', {
        'form':form


    
    })

def profile(request, alumni_id):

    profile = Profile.objects.get(user=alumni_id)
    
    return render(request, 'Reg/profile.html', {
        'profile': profile
    })





