from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View


class AddTaskView(View):
    def get(self, request):
        return render(request, 'tasks/add_task.html')


class EditTaskView(View):
    def get(self, request):
        return render(request, 'tasks/edit_task.html')
