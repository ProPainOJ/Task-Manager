# Generated by Django 4.1.7 on 2023-03-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Manager', '0005_alter_stagesofexecuting_stage_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskgroups',
            name='group_name',
            field=models.CharField(max_length=50, verbose_name='Название группы'),
        ),
    ]
