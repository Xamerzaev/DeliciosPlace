from django.db import models
from django.urls import reverse
from config import settings


class News(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='users')

    text = models.TextField(max_length=1000,
                            help_text="Введите Ваш отзыв!")

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return '{} {}'.format(self.title, self.author)
