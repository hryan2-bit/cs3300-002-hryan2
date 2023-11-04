from django.db import models
from django.urls import reverse

# Create your models here. 
class AppUser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
    
class Killer(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    user = models.ManyToManyField(AppUser, blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('killer-detail', args=[str(self.id)])
   