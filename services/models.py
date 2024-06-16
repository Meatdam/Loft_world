from django.db import models

NULLABLE = {'blank': True, 'null': True}


class ServicCategory(models.Model):
    """
    Создание модели в БД "ServicCategory", прямая связь с таблицей "LoftService" через "category"
    """
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='services/', verbose_name='Картинка', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуг'


class LoftService(models.Model):
    """
    Создание модели в БД "LoftService", прямая связь с таблицей "ServicCategory" через "category"
    """
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='services/', verbose_name='Картинка', **NULLABLE)
    category = models.ForeignKey(ServicCategory, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
