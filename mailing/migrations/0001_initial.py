# Generated by Django 5.0.6 on 2024-06-15 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержание')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Recipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_datetime', models.DateTimeField(auto_now_add=True, verbose_name='начало рассылки')),
                ('next_datetime', models.DateTimeField(blank=True, null=True, verbose_name='next_datetime')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='конец рассылки')),
                ('sending_period', models.CharField(choices=[('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц')], max_length=50, verbose_name='период рассылки')),
                ('settings_status', models.CharField(choices=[('Create', 'Создана'), ('Started', 'Отправлено'), ('Done', 'Завершена')], default='Create', max_length=50, verbose_name='статус рассылки')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingmessage', verbose_name='сообщения')),
                ('recipients', models.ManyToManyField(to='mailing.recipients', verbose_name='получатели')),
            ],
            options={
                'verbose_name': 'Настройка отправки',
                'verbose_name_plural': 'Настройки отправки',
            },
        ),
        migrations.CreateModel(
            name='MailingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_datetime', models.DateTimeField(auto_now_add=True, verbose_name='последняя дата отправки')),
                ('status', models.CharField(choices=[('success', 'успешно'), ('fail', 'неуспешно')], default='', max_length=50, verbose_name='статус попытки')),
                ('mailing_response', models.TextField(verbose_name='ответ сервера')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='рассылка')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.recipients', verbose_name='клиент рассылки')),
            ],
            options={
                'verbose_name': 'Статус отправки',
                'verbose_name_plural': 'Статусы отправки',
            },
        ),
    ]
