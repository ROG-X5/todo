from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Task

def home(request):
    form = TodoForm()
    context = {
        "title": Task.objects.all(),
        "form": form,
    }
    return render(request, 'index.html', context)

@require_POST
def addTask(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Task(title=request.POST['text'])
        new_todo.save()
    return redirect('home')

def completeTodo(request, task_id):
    todo = Task.objects.get(pk=task_id)
    todo.completed = True
    todo.save()
    return redirect('home')

def deleteComplete(request):
    Task.objects.filter(completed__exact=True).delete()

    return redirect('home')