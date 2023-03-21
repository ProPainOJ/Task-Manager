from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()


class Task(models.Model):
    priorities = [
        ('Неважные', 'Неважные и несрочные.'),
        ('Срочно-Неважные', 'Неважные и срочные.'),
        ('Важные', 'Важные и несрочные.'),
        ('Срочно-Важные', 'Важные и срочные.'),
    ]

    task_owner = models.ForeignKey(USER, verbose_name='Пользователь задачи', on_delete=models.CASCADE)
    title_task = models.CharField('Название задачи', max_length=50, )
    task_goal = models.CharField('Цель задачи', null=True, blank=True, max_length=50, )
    task_descriptions = models.TextField('Описание задачи', null=True, blank=True, max_length=600, )
    create_data = models.DateTimeField('Дата создания', auto_now_add=True)
    task_data_goal = models.DateField('Дата выполнения', blank=False)
    priority = models.CharField('Приоритет задачи', choices=priorities, max_length=15, default='Неважные')
    group = models.ForeignKey('TaskGroups', null=True, blank=True, verbose_name='Группа задачи',
                              on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.task_owner}, {self.title_task}'


class TaskGroups(models.Model):
    creator_group = models.ForeignKey(USER, verbose_name='Создатель группы', on_delete=models.CASCADE)
    group_name = models.CharField('Название группы', max_length=50, )
    description_group = models.CharField('Описание группы', blank=True, max_length=150)

    class Meta:
        verbose_name = 'Группа задач'
        verbose_name_plural = 'Группы задач'

    def __str__(self):
        return f'{self.group_name}'


class StagesOfExecuting(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    stage_name = models.CharField('Описание подзадачи', max_length=50)
    stage_name_status = models.BooleanField('Статус подзадачи', default=False)

    class Meta:
        verbose_name = 'Подпункт задачи'
        verbose_name_plural = 'Подпункты задачи'

    def __str__(self):
        return 'Подзадача не выполнена.' if not self.stage_name_status else 'Подзадача завершина.'
