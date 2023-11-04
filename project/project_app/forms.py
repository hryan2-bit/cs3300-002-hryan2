from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Killer, AppUser


#create class for project form
class AppUserForm(ModelForm):
    class Meta:
        model = AppUser
        fields = ('name', 'killer',)
    killer = ModelMultipleChoiceField(
        queryset=Killer.objects.all(), 
        widget=CheckboxSelectMultiple, 
        required=False,
    )

class KillerForm(ModelForm):
    class Meta:
        model = Killer
        fields = ('title',)
