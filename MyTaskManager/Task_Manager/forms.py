from Task_Manager.models import Task, TaskGroups, StagesOfExecuting
from django.forms import modelformset_factory
from django import forms


class CreateTaskForm(forms.ModelForm):
    class Meta(object):
        model = Task
        exclude = [
            'task_owner',
        ]


class CreateNewTaskGroupForm(forms.ModelForm):
    class Meta(object):
        model = TaskGroups
        exclude = [
            'creator_group',
        ]


class CreateStagesOfExecuting(forms.ModelForm):
    class Meta(object):
        model = StagesOfExecuting
        fields = '__all__'


TasksFormSet = modelformset_factory(StagesOfExecuting,
                                    form=CreateStagesOfExecuting,
                                    extra=0,
                                    exclude=('task',),
                                    can_delete=True)
