from django.urls import path
from .views import TaskList,TaskDetail,TaskCreat,TaskUpdate,TaskDelete,CostumLoginView
from django.contrib.auth.views import LogoutView 



urlpatterns = [
 path('Login/',CostumLoginView.as_view(),name='login'),
 path('Logout/',LogoutView.as_view(next_page='login'),name='logout'),

 path('',TaskList.as_view(),name='tasks'),
 path('task-creat/',TaskCreat.as_view(),name='task_creat'),

 path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
 path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task_update'),
 path('task_delete/<int:pk>/',TaskDelete.as_view(),name='task_delete'),



]