from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import UserRegisterForm


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        return render(request, 'users/register.html', {'form': form})


class LoginView(TemplateView):
    template_name = "users/login.html"
