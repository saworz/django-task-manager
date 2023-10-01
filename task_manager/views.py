from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from tasks.models import Tasks


class HomePageView(View):
    template_name = 'task_manager/main_page.html'

    def get(self, request):
        tasks = Tasks.objects.all()
        context = {'tasks': tasks}
        return render(request, self.template_name, context)


class AboutPageView(TemplateView):
    template_name = 'task_manager/about.html'
