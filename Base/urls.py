from django.urls import path
from .views import TaskList,TaskDetail,TaskCreat



urlpatterns = [
 path('',TaskList.as_view(),name='tasks'),
 path('task-creat/',TaskCreat.as_view(),name='task_creat'),

 path('task/<int:pk>/',TaskDetail.as_view(),name='task')

]