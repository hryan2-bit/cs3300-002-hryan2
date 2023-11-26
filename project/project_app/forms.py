from django.forms import ModelForm
from .models import AppUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create class for project form
class AppUserForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ('name', 'killer', 'perk')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']