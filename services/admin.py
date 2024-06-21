from django.contrib import admin

from services.models import ServicCategory, LoftService


@admin.register(ServicCategory)
class ServicCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    list_filter = ('title',)


@admin.register(LoftService)
class LoftServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'category', 'price', 'views_count', 'created_at')
    list_filter = ('title',)
