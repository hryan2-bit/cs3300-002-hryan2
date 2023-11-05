from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Killer, AppUser, Perks


#create class for project form
class AppUserForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ('name', 'killer', 'perk')
    killer = ModelMultipleChoiceField(
        queryset=Killer.objects.all(), 
        widget=CheckboxSelectMultiple, 
        required=True,
    )
    perk = ModelMultipleChoiceField(
        queryset=Perks.objects.all(), 
        widget=CheckboxSelectMultiple, 
        required=True,
    )
