from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView, DetailView, CreateView
from datetime import datetime, timedelta
from .forms import AddTaskForm
from .models import Tasks


# class AddTaskView(View):
#     template_name = "tasks/add_task.html"
#     default_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
#
#     def get(self, request):
#         default_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
#         return render(request, self.template_name,
#                       {'default_date': self.default_date})
#
#     def post(self, request):
#         form = AddTaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('task_manager:home-page')
#         return render(request, self.template_name, {'default_date': self.default_date})

class AddTaskView(CreateView):
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


class TaskDetailView(DetailView):
    template_name = "tasks/single_task.html"
    model = Tasks
