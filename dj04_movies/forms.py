from .models import Movies
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['movie_name', 'short_description', 'review', 'author']
        widgets = {
            'movie_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор отзыва'}),

        }

