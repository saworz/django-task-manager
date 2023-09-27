from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "users"
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile_update/', views.ProfileUpdateView.as_view(), name="profile-update"),
]
