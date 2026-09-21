from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.CharField(max_length=200, verbose_name='Автор')
    cover_class = models.CharField(max_length=20, default='one', verbose_name='Цвет обложки')
    cover_text = models.TextField(default='', verbose_name='Текст на обложке')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title} — {self.author}'