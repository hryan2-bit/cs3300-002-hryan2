from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib import messages
from django.urls import reverse
from typing import Any

# Create your views here.
def index(request):
   users = AppUser.objects.all()
   print("user query set", users)
   return render(request, 'project_app/index.html', {'users':users})

# generic list and detail views
class KillerListView(generic.ListView):
   model = Killer

class KillerDetailView(generic.DetailView):
    model = Killer

class UserListView(generic.ListView):
   model = AppUser

class UserDetailView(generic.DetailView):
   model = AppUser
