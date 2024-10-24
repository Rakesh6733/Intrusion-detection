from django.db.models.signals import post_save
from .models import U, Profile
from django.dispatch import receiver

# Think like:- when the user is created and saved then send the signal,
# and this signal is received by the receiver(create_profile) which is the 
# decorator of the create_profile. This post_save sends the following arguments

@receiver(post_save, sender=U)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=U)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()