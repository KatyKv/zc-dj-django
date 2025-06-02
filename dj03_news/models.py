from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsPost(models.Model):
    title = models.CharField('Заголовок новости')
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Текст новости')
    publication_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', null=True)

    def __str__(self):
        return f'{self.title}, {self.publication_date}, {self.author}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
