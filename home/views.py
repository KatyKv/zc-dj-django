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
        {
            'name': 'Урок 3 - dj03_news / Урок 4 - dj04_forms_news ',
            'url': reverse('dj03_news:index'),
            'description': 'Урок 3 - Работа с моделями: создание, миграции, связь с пользователями и '
                           'вывод данных. Урок 4 - Работа с формой: создание новости',
        },
        {
            'name': 'Урок 4 - dj04_movies',
            'url': reverse('dj04_movies:index'),
            'description': 'Урок 4 - Работа с формой: создание отзыва к фильму',
        },
    ]
    return render(request, 'home/index.html', {'lessons': lessons})