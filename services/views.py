from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

from common.views import TitleMixin
from services.forms import ServicCategoryForm, LoftServiceForm
from services.models import ServicCategory, LoftService


class ServicCategoryListView(TitleMixin, ListView):
    """
    Класс для отображения списка услуг
    """
    model = ServicCategory
    title = 'Наши услуги'
    fields = ('title', 'description', 'image')

    def get_context_data(self, *args, **kwargs):
        """
        Добавление заголовка в контекст
        """
        context_data = super().get_context_data(*args, **kwargs)
        context_data['services'] = ServicCategory.objects.all()

        return context_data


class ServicCategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, UpdateView):
    """
    Класс для редактирования категории услуги
    """
    model = ServicCategory
    form_class = ServicCategoryForm
    title = 'Редактирование категории услуги'
    success_url = reverse_lazy('services:list')
    permission_required = 'services.change_serviccategory'


class ServicCategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, DeleteView):
    """
    Класс для удаления категории услуги
    """
    model = ServicCategory
    title = 'Удаление категории услуги'
    success_url = reverse_lazy('services:list')
    permission_required = 'services.delete_serviccategory'


class ServicCategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, CreateView):
    model = ServicCategory
    title = 'Создание категории услуги'
    form_class = ServicCategoryForm
    success_url = reverse_lazy('services:list')
    permission_required = 'services.add_serviccategory'


class LoftServiceListView(TitleMixin, ListView):
    """
    Класс для отображения списка услуг
    """
    model = LoftService
    title = 'Наши услуги'
    paginate_by = 8

    def get_queryset(self):
        """
        Переопределяем метод get_queryset для фильтрации товаров по категории
        :param: category_id
        :return: queryset
        """
        queryset = super(LoftServiceListView, self).get_queryset()
        servic_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=servic_id) if servic_id else queryset


class LoftServiceCreateView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, CreateView):
    """
    Класс для создания услуги
    """
    model = LoftService
    title = 'Создание услуги'
    form_class = LoftServiceForm
    success_url = reverse_lazy('services:list_servic')
    permission_required = 'services.add_loftservice'


class LoftServiceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, DeleteView):
    """
    Класс для удаления услуги
    """
    model = LoftService
    title = 'Удаление услуги'
    success_url = reverse_lazy('services:list_servic')
    permission_required = 'services.delete_loftservice'


class LoftServiceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, UpdateView):
    """
    Класс для редактирования услуги
    """
    model = LoftService
    title = 'Редактирование услуги'
    form_class = LoftServiceForm
    permission_required = 'services.change_loftservice'

    def get_success_url(self):
        loft_service = self.get_object()
        return reverse_lazy('services:detail_servic', kwargs={'pk': loft_service.id})


class LoftServiceDetailView(TitleMixin, DetailView):
    """
    Класс для просмотра услуги
    """
    model = LoftService
    title = 'Подробная информация о услуге'

    def get_object(self, queryset=None):
        """
        Переопределение метода "get_object" для фильтрации отзывов
        :return: get_object_or_404(Blog, slug=self.kwargs.get('slug'))
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
