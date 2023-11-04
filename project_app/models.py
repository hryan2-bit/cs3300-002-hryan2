from django.db import models
from django.urls import reverse

# Create your models here. 
class Killer(models.Model):
    #Required
    title = models.CharField(max_length=200, blank=False)
    #Required
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('killer-detail', args=[str(self.id)])
   
class AppUser(models.Model):
    #Required
    name = models.CharField(max_length=200)
    #Required
    killer = models.ManyToManyField(Killer, related_name='users')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
    