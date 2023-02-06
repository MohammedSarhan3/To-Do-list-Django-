from django.urls import path
from .views import TaskList,TaskDetail,TaskCreat,TaskUpdate,TaskDelete,CostumLoginView,RegisterPage,TaskReorder
from django.contrib.auth.views import LogoutView 



urlpatterns = [
 path('Login/',CostumLoginView.as_view(),name='login'),
 path('Logout/',LogoutView.as_view(next_page='login'),name='logout'),
 path('register/', RegisterPage.as_view(), name='register'),


 path('',TaskList.as_view(),name='tasks'),
 path('taskcreat/',TaskCreat.as_view(),name='task-create'),

 path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
 path('taskupdate/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
 path('taskdelete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
 path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),



]