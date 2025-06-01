from django.shortcuts import render
from django.urls import reverse

def index(request):
    lessons = [
        {
            'name': 'Урок 1 - dj01',
            'url': reverse('dj01:index'),
            'description': 'Первые шаги: создание приложения, маршруты и простые страницы.',
        },
        {
            'name': 'Урок 2 - dj02',
            'url': reverse('dj02:index'),
            'description': 'Шаблоны и статические файлы: как красиво оформить сайт.',
        },
    ]
    return render(request, 'home/index.html', {'lessons': lessons})