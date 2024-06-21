from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Класс для отображения модели Blog в админке.
    """
    list_display = ('title', 'description', 'image', 'owner')
