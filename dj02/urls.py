from django.urls import path
from . import views

app_name = 'dj02'

urlpatterns = [
    path("", views.index, name='index'),
    path('day1', views.day1, name='day1'),
    path('day2', views.day2, name='day2'),
    path('day3', views.day3, name='day3')
]