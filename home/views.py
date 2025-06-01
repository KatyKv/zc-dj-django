from django.shortcuts import render
from django.urls import reverse

def index(request):
    lessons = [
        {'url': reverse('dj01:index'), 'name': 'dj01'},
        {'url': reverse('dj02:index'), 'name': 'dj02'},
    ]
    return render(request, 'home/index.html', {'lessons': lessons})
