from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import AppUserForm, KillerForm
from django.contrib import messages   
from django.urls import reverse
from typing import Any

# Create your views here.
def index(request):
   users = AppUser.objects.all()
   print("user query set", users)
   return render(request, 'project_app/index.html', {'users':users})

def createUser(request):
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
  if request.method == 'POST':
    form = KillerForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      return redirect('project-detail', pk=user_id)
  else:
    form = KillerForm(instance=user)
    context={
     'form': form,
     'user': user,
    }
  return render(request, 'project_app/killer_update.html', context)

def deleteUser(request, user_id):
   user = get_object_or_404(AppUser, pk=user_id)
   if request.method == 'POST':
      user.delete()
      # Redirect back to the index
      return redirect('index')

   context = {'user': user}
   return render(request, 'project_app/user_delete.html', context)

# generic list and detail views
class KillerListView(generic.ListView):
   model = Killer

class KillerDetailView(generic.DetailView):
    model = Killer

class UserListView(generic.ListView):
   model = AppUser

class UserDetailView(generic.DetailView):
   model = AppUser

   def get_context_data(self, **kwargs):
      context = super(UserDetailView, self).get_context_data(**kwargs)
      user = self.get_object()
      killers_list = user.killer.all()  # access the related killers through the 'killers' many-to-many field
      context['k_list'] = killers_list
      return context
   