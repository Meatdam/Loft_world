from django.contrib import admin

from mailing.models import Recipients, MailingMessage, MailingSettings, MailingStatus


@admin.register(Recipients)
class RecipientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'description')
    list_filter = ('name',)


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('first_datetime', 'end_time', 'sending_period','message','settings_status')


@admin.register(MailingStatus)
class MailingStatusAdmin(admin.ModelAdmin):
    list_filter = ('last_datetime', 'status', 'mailing_response', 'mailing_list', 'recipient')

