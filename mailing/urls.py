from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import RecipientsCreateView, RecipientsListView, RecipientsDeleteView, RecipientsDetailView, \
    MailingMessageCreateView, MailingMessageListView, MailingMessageDeleteView, MailingMessageUpdateView, \
    MailingMessageDetailView

app_name = MailingConfig.name


urlpatterns = [
    # Клиент
    path('recipients/', RecipientsCreateView.as_view(), name='recipients'),
    path('recipients_list/', RecipientsListView.as_view(), name='recipients_list'),
    path('recipients_delete/<int:pk>/', RecipientsDeleteView.as_view(), name='recipients_delete'),
    path('recipients_detail/<int:pk>/', RecipientsDetailView.as_view(), name='recipients_detail'),
    # Сообщение для рассылки
    path('message_create/', MailingMessageCreateView.as_view(), name='message_create'),
    path('message_list/', MailingMessageListView.as_view(), name='message_list'),
    path('message_delete/<int:pk>/', MailingMessageDeleteView.as_view(), name='message_delete'),
    path('message_update/<int:pk>/', MailingMessageUpdateView.as_view(), name='message_update'),
    path('message_detail/<int:pk>/', MailingMessageDetailView.as_view(), name='message_detail'),
]