# Generated by Django 4.1.7 on 2023-03-22 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Manager', '0011_alter_task_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.ForeignKey(blank=True, default='Standard group', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Task_Manager.taskgroups', verbose_name='Группа задачи'),
        ),
    ]
