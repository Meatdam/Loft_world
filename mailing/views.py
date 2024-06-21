from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from common.views import TitleMixin
from mailing.forms import RecipientsForm, MailingMessageForm, MailingSettingsForm
from mailing.models import Recipients, MailingMessage, MailingSettings, MailingStatus


class RecipientsCreateView(TitleMixin, CreateView):
    """
    Класс для отображения формы создания клиента
    """
    model = Recipients
    form_class = RecipientsForm
    title = 'Обратная связь'
    success_url = reverse_lazy('loft:index')


class RecipientsListView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, ListView):
    """
    Класс для отображения списка клиентов которые подписываются на рассылку
    """
    model = Recipients
    title = 'Список клиентов'
    permission_required = 'mailing.view_recipients'


class RecipientsDetailView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, DetailView):
    """
    Класс для отображения подробной информации о клиенте
    """
    model = Recipients
    title = 'Подробная информация о клиенте'
    success_url = reverse_lazy('mailing:recipients_list')
    permission_required = 'mailing.view_recipients'


class RecipientsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, DeleteView):
    """
    Класс для удаления клиента из списка рассылки
    """
    model = Recipients
    title = 'Удаление клиента'
    success_url = reverse_lazy('mailing:recipients_list')
    permission_required = 'mailing.delete_recipients'


class MailingMessageCreateView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, CreateView):
    """
    Класс для отображения формы создания сообщения для рассылки
    """
    model = MailingMessage
    form_class = MailingMessageForm
    title = 'Создание сообщения для рассылки'
    success_url = reverse_lazy('mailing:message_list')
    permission_required = 'mailing.add_mailingmessage'


class MailingMessageListView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, ListView):
    """
    Класс для отображения списка рассылок
    """
    model = MailingMessage
    title = 'Список рассылок'
    permission_required = 'mailing.view_mailingmessage'


class MailingMessageDetailView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, DetailView):
    """
    Класс для отображения подробной информации сообщения о рассылке
    """
    model = MailingMessage
    title = 'Подробная информация о рассылке'
    success_url = reverse_lazy('mailing:message_list')
    permission_required = 'mailing.view_mailingmessage'


class MailingMessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, DeleteView):
    """
    Класс для удаления сообщения рассылки из списка рассылок
    """
    model = MailingMessage
    title = 'Удаление рассылки'
    success_url = reverse_lazy('mailing:message_list')
    permission_required = 'mailing.delete_mailingmessage'


class MailingMessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, UpdateView):
    """
    Класс для редактирования сообщения рассылки
    """
    model = MailingMessage
    title = 'Редактирование рассылки'
    form_class = MailingMessageForm
    permission_required = 'mailing.change_mailingmessage'

    def get_success_url(self):
        return reverse_lazy('mailing:settings_detail', kwargs={'pk': self.get_object().id})


class MailingSettingsListView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, ListView):
    """
    Класс для отображения списка рассылок
    """
    model = MailingSettings
    title = 'Список рассылок'
    permission_required = 'mailing.view_mailingsettings'


class MailingSettingsCreateView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, CreateView):
    """
    Класс для отображения формы создания рассылки
    """
    model = MailingSettings
    form_class = MailingSettingsForm
    title = 'Создание рассылки'
    success_url = reverse_lazy('mailing:settings_list')
    permission_required = 'mailing.add_mailingsettings'


class MailingSettingsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, UpdateView):
    """
    Класс для редактирования рассылки
    """
    model = MailingSettings
    title = 'Редактирование рассылки'
    form_class = MailingSettingsForm
    permission_required = 'mailing.change_mailingsettings'

    def get_success_url(self):
        return reverse_lazy('mailing:settings_detail', kwargs={'pk': self.get_object().id})


class MailingSettingsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, DeleteView):
    """
    Класс для удаления рассылки из списка рассылок
    """
    model = MailingSettings
    title = 'Удаление рассылки'
    success_url = reverse_lazy('mailing:settings_list')
    permission_required = 'mailing.delete_mailingsettings'


class MailingSettingsDetailView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, DetailView):
    """
    Класс для отображения подробной информации о рассылке
    """
    model = MailingSettings
    title = 'Подробная информация о рассылке'
    success_url = reverse_lazy('mailing:settings_list')
    permission_required = 'mailing.view_mailingsettings'


class MailingStatusListView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, ListView):
    """
    Класс для отображения логов рассылок
    """
    model = MailingStatus
    title = 'Логи рассылок'
    permission_required = 'mailing.view_mailingstatus'


class MailingStatusDetailView(LoginRequiredMixin, PermissionRequiredMixin, TitleMixin, DetailView):
    """
    Класс для отображения подробной информации о статусе рассылки
    """
    model = MailingStatus
    title = 'Подробная информация о статусе рассылки'
    success_url = reverse_lazy('mailing:status_list')
    permission_required = 'mailing.view_mailingstatus'
