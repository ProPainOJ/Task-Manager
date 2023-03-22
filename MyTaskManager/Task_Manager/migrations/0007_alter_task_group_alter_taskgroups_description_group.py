# Generated by Django 4.1.7 on 2023-03-21 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Manager', '0006_alter_taskgroups_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.ForeignKey(blank=True, default='No Groups', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Task_Manager.taskgroups', verbose_name='Группа задачи'),
        ),
        migrations.AlterField(
            model_name='taskgroups',
            name='description_group',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Описание группы'),
        ),
    ]
