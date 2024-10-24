from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', views.reg, name='reg'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('gallery/', views.gallery, name='gallery'),
    path('alumni/', views.alumni, name='alumni'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('jobs/', views.jobs, name='jobs'),
    path('jobform', views.jobform,name='jobform'),
    path('form/', views.form, name="form"),
    path('alumni/<str:alumni_id>/', views.profile, name="profile"),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
