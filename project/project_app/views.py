from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages   
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import AppUserForm, CreateUserForm
from typing import Any
from .decorators import allowed_users

import requests

# Create your views here.

# API Exploration
def apiExploration(request):
   response = requests.get('http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=381210') #gets the new updates for Dead By Daylight
   updates = response.json()
   #print(updates)
   return render(request, 'project_app/api_update.html', {'updates': updates})

# FULL PROJECT DO NOT TOUCH BELOW THIS
def index(request):
   users = AppUser.objects.all()
   print("user query set", users)
   return render(request, 'project_app/index.html', {'users':users})

@login_required(login_url='login')
@allowed_users(allowed_roles=['student_role'])
def userPage(request):
   appuser = request.user.appuser
   form = AppUserForm(instance=appuser)
   print('user', appuser)
   if request.method == 'POST':
      form = AppUserForm(request.POST, request.FILES, instance=appuser)
      if form.is_valid():
         form.save()
   context = {'form': form}
   return render(request, 'project_app/user.html', context)

def createUser(request):
   # if the form is submitted
   if request.method == 'POST':
      form = AppUserForm(request.POST.copy())
      if form.is_valid():
         form.save()
         return redirect('index')
   else:
      form = AppUserForm()
   print(form.fields)
   context = {'form': form}
   return render(request, 'project_app/create_user.html', context)

def updateKillerList(request, user_id):
  user = get_object_or_404(AppUser, pk=user_id)
  # if the form is submitted
  if request.method == 'POST':
    form = AppUserForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      return redirect('user-detail', pk=user_id)
  else:
    form = AppUserForm(instance=user)
    context={
     'form': form,
     'user': user,
    }
  return render(request, 'project_app/update_killer.html', context)

def deleteUser(request, user_id):
   user = get_object_or_404(AppUser, pk=user_id)
   # if the form is submitted
   if request.method == 'POST':
      user.delete()
      # Redirect back to the index
      return redirect('index')

   context = {'user': user}
   return render(request, 'project_app/user_delete.html', context)

def registerPage(request):
   form = CreateUserForm()
   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         user = form.save()
         username = form.cleaned_data.get('username')
         group = Group.objects.get(name='user__role')
         user.groups.add(group)

         messages.success(request, 'Account was created for ' + username)
         return redirect('login')
   context = {'form': form}
   return render(request, 'registration/register.html', context)


# generic list and detail views
class KillerListView(generic.ListView):
   model = Killer

class KillerDetailView(generic.DetailView):
   model = Killer

class PerkListView(generic.ListView):
   model = Perks

class PerkDetailView(generic.DetailView):
   model = Perks

class UserListView(LoginRequiredMixin, generic.ListView):
   model = AppUser

class UserDetailView(LoginRequiredMixin, generic.DetailView):
   model = AppUser

   def get_context_data(self, **kwargs):
      context = super(UserDetailView, self).get_context_data(**kwargs)
      user = self.get_object()
      killers_list = user.killer.all()  # access the related killers through the 'killers' many-to-many field
      context['k_list'] = killers_list
      perks_list = user.perk.all()
      context['p_list'] = perks_list
      return context
   