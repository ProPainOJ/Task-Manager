# Generated by Django 4.1.7 on 2023-03-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0014_alter_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(blank=True, error_messages={'blank', 'Ну хз что это'}, max_length=150, null=True, verbose_name='username'),
        ),
    ]
