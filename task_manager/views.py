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

    def get_queryset(self):
        return Tasks.objects.filter(author=self.request.user.pk).order_by(self.ordering)

    def get(self, request, *args, **kwargs):
        if request.GET.get("sort"):
            self.ordering = request.GET.get("sort")

        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        context = self.get_context_data()
        return self.render_to_response(context)


class AboutPageView(TemplateView):
    template_name = 'task_manager/about.html'
