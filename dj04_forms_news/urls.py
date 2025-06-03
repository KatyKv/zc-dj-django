from django.urls import path
from . import views

app_name = 'dj04_forms_news'

urlpatterns = [
    path("add_article/", views.add_article, name='add_article'),
]