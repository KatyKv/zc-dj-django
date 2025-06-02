from django.urls import path
from . import views

app_name = 'dj03_news'

urlpatterns = [
    path("", views.index, name='index'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
]