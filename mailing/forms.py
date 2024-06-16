from django import forms

from common.views import StyleFormMixin, TitleMixin
from mailing.models import Recipients, MailingMessage


class RecipientsForm(StyleFormMixin, forms.ModelForm):
    """
    Модель клиентов которые подписываются на рассылку
    """
    class Meta:
        model = Recipients
        fields = ('email', 'name', 'description')


class MailingMessageForm(StyleFormMixin, forms.ModelForm):
    """
    Модель сообщения для рассылки
    """
    class Meta:
        model = MailingMessage
        fields = ('title', 'content')
