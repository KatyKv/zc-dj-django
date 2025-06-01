from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# ВАЖНО! request - обязательный параметр!
def index(request):
    return HttpResponse(
        '<h1>Первый проект на Django</h1>'
        '<p><a href="/dj01/data">Ссылка на страницу /data</a></p>'
        '<p><a href="/dj01/test">Ссылка на страницу /test</a></p>'
    )

def new(request):
    return HttpResponse('<h2>Вторая страница проекта</h2>')

def datapage(request):
    return HttpResponse(
        '<h1>Страница данных</h1>'
        '<h2>Здесь может быть какая-то информация</h2>'
    )

def testpage(request):
    return HttpResponse(
        '<h2>Тестовая страница</h2>'
        '<p>Выведем расчёт:</p>'
        f'<p>Число 2 в степени 128 =  {2 ** 128}<p>'
    )
