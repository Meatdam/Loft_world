from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from common.views import TitleMixin
from mailing.forms import RecipientsForm, MailingMessageForm
from mailing.models import Recipients, MailingMessage


class RecipientsCreateView(TitleMixin, CreateView):
    """
    Класс для отображения формы создания клиента
    """
    model = Recipients
    form_class = RecipientsForm
    title = 'Обратная связь'
    success_url = reverse_lazy('loft:index')


class RecipientsListView(TitleMixin, ListView):
    """
    Класс для отображения списка клиентов которые подписываются на рассылку
    """
    model = Recipients
    title = 'Список клиентов'


class RecipientsDetailView(TitleMixin, DetailView):
    """
    Класс для отображения подробной информации о клиенте
    """
    model = Recipients
    title = 'Подробная информация о клиенте'
    success_url = reverse_lazy('mailing:recipients_list')


class RecipientsDeleteView(TitleMixin, DeleteView):
    """
    Класс для удаления клиента из списка рассылки
    """
    model = Recipients
    title = 'Удаление клиента'
    success_url = reverse_lazy('mailing:recipients_list')


class MailingMessageCreateView(TitleMixin, CreateView):
    """
    Класс для отображения формы создания сообщения для рассылки
    """
    model = MailingMessage
    form_class = MailingMessageForm
    title = 'Создание сообщения для рассылки'
    success_url = reverse_lazy('mailing:message_list')


class MailingMessageListView(TitleMixin, ListView):
    """
    Класс для отображения списка рассылок
    """
    model = MailingMessage
    title = 'Список рассылок'


class MailingMessageDetailView(TitleMixin, DetailView):
    """
    Класс для отображения подробной информации сообщения о рассылке
    """
    model = MailingMessage
    title = 'Подробная информация о рассылке'
    success_url = reverse_lazy('mailing:message_list')


class MailingMessageDeleteView(TitleMixin, DeleteView):
    """
    Класс для удаления сообщения рассылки из списка рассылок
    """
    model = MailingMessage
    title = 'Удаление рассылки'
    success_url = reverse_lazy('mailing:message_list')


class MailingMessageUpdateView(TitleMixin, UpdateView):
    """
    Класс для редактирования сообщения рассылки
    """
    model = MailingMessage
    title = 'Редактирование рассылки'
    form_class = MailingMessageForm

    def get_success_url(self):
        return reverse_lazy('mailing:message_detail', kwargs={'pk': self.get_object().id})
