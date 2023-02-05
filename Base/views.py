from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Task
from django.shortcuts import  redirect
# Create your views here.



class TaskList(ListView):
    model=Task
    context_object_name='tasks'



