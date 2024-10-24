from django.contrib.auth.backends import BaseBackend
from .models import U

class CustomAuthBackend(BaseBackend):
    # It authenticates the email and password and returns the user.
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = U.objects.get(email=email)
        except U.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        else:
            return None
        
    def get_user(self, user_id):
        try:
            return U.objects.get(pk=user_id)
        except U.DoesNotExist:
            return None
        
    

