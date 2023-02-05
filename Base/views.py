from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.views import LoginView,login 
from .models import Task
from django.urls import  reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CostumLoginView(LoginView):
    template_name='user/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self) :
        return reverse_lazy('tasks')

class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='tasks'


class TaskDetail(DetailView):
    model=Task
    context_object_name='task'

class TaskCreat(CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasks')

