from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')
    preview = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    price_per_one = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за штуку')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_of_change = models.DateTimeField(auto_now=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name', '-date_of_creation',)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)
