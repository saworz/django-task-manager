from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta
from .forms import AddTaskForm
from .models import Tasks


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


class UpdateTaskView(AddTaskView, UpdateView):
    pass


class TaskDetailView(DetailView):
    template_name = "tasks/single_task.html"
    model = Tasks


class DeleteTaskView(DeleteView):
    template_name = ""