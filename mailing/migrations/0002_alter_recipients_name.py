# Generated by Django 5.0.6 on 2024-06-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipients',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Имя'),
        ),
    ]
