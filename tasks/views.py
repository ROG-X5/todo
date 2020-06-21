from django.views.generic import ListView

from .models import Task

class Index(ListView):
    model = Task
    template_name = 'index.html'