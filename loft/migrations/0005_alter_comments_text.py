# Generated by Django 5.0.6 on 2024-05-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loft', '0004_rename_user_comments_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(),
        ),
    ]
