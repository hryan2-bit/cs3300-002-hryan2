from django.contrib import admin
from .models import Killer, AppUser, Perks

# Register your models here.
admin.site.register(Killer)
admin.site.register(AppUser)
admin.site.register(Perks)