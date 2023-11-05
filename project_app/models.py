from django.db import models
from django.core.files.storage import FileSystemStorage
from django.urls import reverse

fs = FileSystemStorage(location="/media")

# Create your models here. 
class Killer(models.Model):
    #Required
    title = models.CharField(max_length=200, blank=False)
    #Required
    description = models.TextField(blank=False)
    photo = models.ImageField(upload_to="media/killers/", blank=False)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('killer-detail', args=[str(self.id)])
   
class Perks(models.Model):
    #Required
    title = models.CharField(max_length=200, blank=False)
    #Required
    description = models.TextField(blank=False)
    photo = models.ImageField(upload_to="media/perks/", blank=False)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('perk-detail', args=[str(self.id)])

class AppUser(models.Model):
    #Required
    name = models.CharField(max_length=200)
    killer = models.ManyToManyField(Killer, related_name='users', blank=False)
    perk = models.ManyToManyField(Perks, related_name='users', blank=False)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
    