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

    IMPORTANCE_MAPPING = {
        "high": 3,
        "medium": 2,
        "low": 1,
    }

    def importance_sort_key(self, task, order=None):
        if self.request.session.get('ordering') == "-importance":
            return -self.IMPORTANCE_MAPPING.get(task.importance, 0)
        return self.IMPORTANCE_MAPPING.get(task.importance, 0)

    def get_queryset(self):
        ordering = self.request.session.get('ordering', "deadline")
        queryset = Tasks.objects.filter(author=self.request.user.pk)

        if ordering == "importance" or ordering == "-importance":
            queryset = sorted(queryset, key=self.importance_sort_key)
        else:
            queryset = queryset.order_by(ordering)

        return queryset

    def get(self, request, *args, **kwargs):
        current_ordering = self.request.GET.get('sort')
        if current_ordering:
            if current_ordering == self.request.session.get("ordering"):
                self.request.session["ordering"] = '-' + current_ordering
            else:
                self.request.session["ordering"] = current_ordering
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)


class AboutPageView(TemplateView):
    template_name = 'task_manager/about.html'
