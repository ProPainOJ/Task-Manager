# Generated by Django 4.1.7 on 2023-03-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_avatar',
            field=models.ImageField(default='', max_length=250, upload_to='avatars/%Y'),
        ),
    ]
