from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='blog/', verbose_name='картинка', **NULLABLE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
