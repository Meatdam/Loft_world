from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin

from common.views import TitleMixin
from loft.forms import CategoryForm, ProductForm, CommentsForm
from loft.models import Category, Product


class IndexListView(TitleMixin, ListView):
    model = Category
    fields = ('name', 'description', 'image')
    title = 'Главная'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['categories'] = Category.objects.all()

        return context_data


class ProductListView(TitleMixin, ListView):
    """
    Класс для отображения списка товаров
    model = Product
    paginate_by = 6
    title = 'Главная'
    """
    model = Product
    paginate_by = 8
    title = 'Продукция'
    # template_name = 'loft/product_list.html'

    def get_queryset(self):
        """
        Переопределяем метод get_queryset для фильтрации товаров по категории
        :param: category_id
        :return: queryset
        """
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


class CategoryCreateView(TitleMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('loft:index')
    title = 'Добавление категории'


class CategoryUbdateView(TitleMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('loft:index')
    title = 'Редактирование категории'


class CategoryDeleteView(TitleMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('loft:index')
    title = 'Удаление категории'


class ProductCreateView(TitleMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('loft:index')
    title = 'Добавление продукта'


class ProductDeleteView(TitleMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('loft:index')
    title = 'Удаление продукта'


class ProductUpdateView(TitleMixin, UpdateView):
    model = Product
    form_class = ProductForm
    title = 'Редактирование продукта'

    def get_success_url(self):
        return reverse_lazy('loft:product', kwargs={'category_id': self.object.category_id})


class ProductDetailView(FormMixin, TitleMixin, DetailView):
    model = Product
    title = 'Подробная информация о продукте'
    form_class = CommentsForm

    def get_success_url(self):
        return reverse_lazy('loft:view', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        """
        Переопределение метода "post" для сохранения комментария
        :param: request
        :param: *args
        :param: **kwargs
        :return: super().post(request, *args, **kwargs)
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_object(self, queryset=None):
        """
        Переопределение метода "get_object" для фильтрации отзывов
        :return: get_object_or_404(Blog, slug=self.kwargs.get('slug'))
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        print('get_object')
        return self.object

    def form_valid(self, form):
        """
        Переопределение метода "form_valid" для сохранения комментария
        :param: form
        :return: super().form_valid(form)
        """
        object = form.save(commit=False)
        object.product = self.get_object()
        object.owner = self.request.user
        object.save()
        return super().form_valid(form)
