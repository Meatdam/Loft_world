from django import forms

from common.views import StyleFormMixin
from loft.models import Category, Product, Comments


class CategoryForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description', 'image')


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price', 'quantity',)


class CommentsForm(forms.ModelForm):
    """
    Класс для работы с формой "CommentsForm"
    """
    class Meta:
        model = Comments
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control bg-dark text-white',
                                          'placeholder': 'Текст комментария:', 'rows': '5',
                                          'style': 'border-radius: 10px'}),
        }
