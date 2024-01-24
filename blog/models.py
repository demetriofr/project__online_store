from django.db import models


NULLABLE = {'blank': True, 'null': True}
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug')
    content = models.TextField(max_length=2000, verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    publication_indicator = models.BooleanField(default=True, verbose_name='признак публикации')
    number_of_view = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} {self.date_create}'

    class Meta:
        verbose_name = 'заголовок'
        verbose_name_plural = 'заголовки'
        ordering = ('title',)
