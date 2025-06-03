from dj03_news.models import NewsPost
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class NewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'short_description', 'text']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Полный текст новости'}),
        }

