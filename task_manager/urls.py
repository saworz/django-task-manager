from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "task_manager"
urlpatterns = [
    path('', views.HomePageView.as_view(), name="home-page"),
    path('about', views.AboutPageView.as_view(), name="about-page"),
]
