from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    data = {
        'title': 'Список дел',
        'tasks': ['dolbaeb','hello','1233'],
        'task': {
            'author': 'Zheka146',
            'task_caption': 'ааа'
        }
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')


