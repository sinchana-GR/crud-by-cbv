from django.shortcuts import render

# Create your views here.
from app.models import *

from django.views.generic import ListView,DetailView,CreateView,UpdateView


class School_list(ListView):
    model=School
    context_object_name='allso'


class School_detail(DetailView):
    model=School
    context_object_name='DOSI'



class School_create(CreateView):
    model=School
    fields="__all__"

class School_update(UpdateView):
    model=School
    fields="__all__"






