from django.shortcuts import render

# Create your views here.
from app.models import *

from django.views.generic import ListView,DetailView


class School_list(ListView):
    model=School
    context_object_name='allso'


class School_detail(DetailView):
    model=School
    context_object_name='DOSI'