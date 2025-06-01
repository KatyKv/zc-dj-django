from django.urls import path
from . import views

app_name = 'dj01'

urlpatterns = [
    path("", views.index, name='index'),
    path('new', views.new, name='new'),
    path('data', views.datapage, name='data'),
    path('test', views.testpage, name='test')
]