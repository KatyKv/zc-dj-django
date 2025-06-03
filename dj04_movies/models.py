from django.db import models

class Movies(models.Model):
    movie_name = models.CharField('Название фильма')
    short_description = models.CharField('Краткое описание фильма', max_length=200)
    review = models.TextField('Отзыв на фильм')
    author = models.CharField('Автор отзыва', max_length=200)

    def __str__(self):
        return f'{self.movie_name}, {self.author}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
