from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from .forms import AddTaskForm
from .models import Tasks
from django.urls import reverse_lazy


class AddTaskView(LoginRequiredMixin, CreateView):
    template_name = "tasks/add_task.html"
    model = Tasks
    fields = ["title", "deadline", "description", "importance"]

    def get_initial(self):
        initial = super().get_initial()
        initial['deadline'] = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        return initial

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(UpdateView):
    model = Tasks
    template_name = "tasks/add_task.html"
    success_url = reverse_lazy("task_manager:home-page")
    fields = ["title", "deadline", "description", "importance"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context


class TaskDetailView(DetailView):
    template_name = "tasks/single_task.html"
    model = Tasks


class DeleteTaskView(DeleteView):
    model = Tasks
    success_url = reverse_lazy("task_manager:home-page")

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs["pk"])

    def get_success_url(self):
        return self.success_url
