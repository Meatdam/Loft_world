from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView

from blog.forms import BlogForm
from blog.models import Blog
from common.views import TitleMixin


class BlogCreateView(LoginRequiredMixin, TitleMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')
    title = 'Создание отзыва'

    def form_valid(self, form):
        """
        Привязывает отзыв к текущему пользователю.
        """
        blog = form.save()
        blog.owner = self.request.user
        blog.save()

        return super().form_valid(form)


class BlogListView(TitleMixin, ListView):
    """
    Класс для отображения списка отзывов
    """
    model = Blog
    title = 'Отзывы'
    paginate_by = 8


class BlogDeleteView(LoginRequiredMixin, TitleMixin, DeleteView):
    """
    Класс для удаления отзыва
    """
    model = Blog
    title = 'Удаление отзыва'
    success_url = reverse_lazy('blog:blog_list')


class BlogDetailView(TitleMixin, DetailView):
    """
    Класс для отображения подробной информации об отзыве
    """
    model = Blog
    title = 'Детали отзыва'


class BlogUpdateView(LoginRequiredMixin, TitleMixin, UpdateView):
    """
    Класс для редактирования отзыва
    """
    model = Blog
    title = 'Редактирование отзыва'
    form_class = BlogForm

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.get_object().id})



