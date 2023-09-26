from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'task_manager/main_page.html'


class AboutPageView(TemplateView):
    template_name = 'task_manager/about.html'
