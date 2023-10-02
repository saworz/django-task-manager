from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import View
from tasks.models import Tasks


class TasksListView(ListView):
    model = Tasks
    template_name = 'task_manager/main_page.html'
    context_object_name = "tasks"
    paginate_by = 5
    ordering = "deadline"


class AboutPageView(TemplateView):
    template_name = 'task_manager/about.html'
