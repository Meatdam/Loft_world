from django import forms

from blog.models import Blog
from common.views import StyleFormMixin


class BlogForm(StyleFormMixin, forms.ModelForm):
    """
    Модель для работы с формой "BlogForm"
    """
    class Meta:
        model = Blog
        fields = ('title', 'description', 'image',)