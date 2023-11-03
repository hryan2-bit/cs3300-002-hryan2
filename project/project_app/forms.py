from django.forms import ModelForm
from .models import Killer

#create class for project form
class KillerForm(ModelForm):
    class Meta:
        model = Killer
        fields = ('name', 'is_active', 'about')