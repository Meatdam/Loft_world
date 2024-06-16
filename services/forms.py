from django import forms

from common.views import StyleFormMixin
from services.models import ServicCategory, LoftService


class ServicCategoryForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = ServicCategory
        fields = ('title', 'description', 'image')


class LoftServiceForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для формы создания услуги
    """
    class Meta:
        model = LoftService
        fields = ('title', 'description', 'image', 'category', 'price')
