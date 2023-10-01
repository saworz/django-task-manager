from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from datetime import datetime, timedelta
from .forms import AddTaskForm


class AddTaskView(View):
    template_name = "tasks/add_task.html"
    default_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')

    def get(self, request):
        form = AddTaskForm()
        default_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        return render(request, self.template_name,
                      {'default_date': self.default_date})

    def post(self, request):
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_manager:home-page')
        return render(request, self.template_name, {'default_date': self.default_date})


class EditTaskView(View):
    template_name = "tasks/edit_task.html"

    def get(self, request):
        return render(request, self.template_name)