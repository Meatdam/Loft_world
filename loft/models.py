from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    Создание модели в БД "Category", прямая связь с таблицей "Product" через "category"
    """
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='category/', verbose_name='картинка', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """
    Создание модели в БД "Product", прямая связь с таблицей "Category" через "category"
    """
    name = models.CharField(max_length=250, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='catalog/', verbose_name='аватар', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.FloatField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(verbose_name='дата изменения', **NULLABLE)

    def __str__(self):
        return f"{self.name} ({self.price})"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Comments(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='продукт', **NULLABLE,
                                related_name='comments_product')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='автор комментария', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    text = models.TextField(verbose_name='текст комментария')
    status = models.BooleanField(default=False, verbose_name='видимость комментария')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
