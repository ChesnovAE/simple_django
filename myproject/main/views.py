from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def get_index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта',
                   'tasks': tasks})


def get_about(request):
    return render(request, 'main/about.html')


def get_create(request):
    error = ''
    if request.method == 'POST':
        data = TaskForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('home')
        else:
            error = 'Invalid form'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
