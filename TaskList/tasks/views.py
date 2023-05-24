from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import UpdateView, DeleteView
# Create your views here.

class TaskDelete(DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = '/tasks/'

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'tasks/create.html'

    form_class = TaskForm

def tasks_home(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_home.html', {'tasks': tasks})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_home')
        else:
            error = 'Поля заполнены неправильно'

    form = TaskForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'tasks/create.html', data)
