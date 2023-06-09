# Generated by Django 4.1.7 on 2023-03-19 12:31

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_alter_myuser_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_avatar',
            field=models.ImageField(blank=True, default='default_avatar/default.png', help_text='Путь файла: MEDIA_ROOT/user_id/category/filename', max_length=250, null=True, upload_to=Users.models.user_directory_path, verbose_name='Фотография пользователя.'),
        ),
    ]
