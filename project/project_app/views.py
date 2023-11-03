from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import KillerForm
from django.contrib import messages
from django.urls import reverse
from typing import Any

# Create your views here.

# generic list and detail views
def index(request):
   return render(request, 'project_app/index.html')

class KillerListView(generic.ListView):
   model = Killer