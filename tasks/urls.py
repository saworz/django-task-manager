from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "tasks"
urlpatterns = [
    path('add/', views.AddTaskView.as_view(), name="add-task"),
    path('<int:pk>/', views.TaskDetailView.as_view(), name="task-view"),
]
