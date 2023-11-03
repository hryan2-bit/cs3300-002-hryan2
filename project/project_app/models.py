from django.db import models
from django.urls import reverse

# Create your models here.
class Killer(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('killer-detail', args=[str(self.id)])