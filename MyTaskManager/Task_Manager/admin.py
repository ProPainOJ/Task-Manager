from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Task, StagesOfExecuting, TaskGroups


class AdminTaskGroup(admin.TabularInline):
    model = StagesOfExecuting
    extra = 0


@admin.register(Task)
class AdminTask(ModelAdmin):
    # readonly_fields = ('task_data_goal', )
    raw_id_fields = ('task_owner',)
    list_display = ('pk', 'title_task', 'task_owner', 'group',)
    list_display_links = ('title_task',)
    inlines = [
        AdminTaskGroup,
    ]


@admin.register(TaskGroups)
class AdminTaskGroup(ModelAdmin):
    fields = (
        'creator_group',
        'group_name',
        'description_group',
    )
