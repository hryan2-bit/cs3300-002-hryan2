from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import AppUser


#create class for project form
class AppUserForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ('name', 'killer', 'perk')

