from .forms import CreateTaskForm, CreateNewTaskGroupForm, TasksFormSet
from .models import Task, StagesOfExecuting, TaskGroups
from django.contrib.auth import mixins, get_user_model
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import *
from django.views import View

USER = get_user_model()


class CreateNewTask(mixins.LoginRequiredMixin, CreateView):
    success_url = 'tasks_home'
    template_name = 'manager/new_task.html'

    model = Task
    form_class = CreateTaskForm

    def clean(self):
        pass

    def get(self, request, *args, **kwargs):
        user_groups = TaskGroups.objects.filter(creator_group=request.user.pk).values_list('id', 'group_name', )
        self.form_class.base_fields.get('group').choices = user_groups
        context = {
            'title': 'Новая задача',
            'form': self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['title_task'] and form.cleaned_data['title_task'] in Task.objects.filter(
                    task_owner=self.request.user.pk).values_list('title_task', flat=True):
                form = CreateTaskForm(request.POST)
                user_groups = TaskGroups.objects.filter(creator_group=request.user.pk).values_list('id', 'group_name', )
                form.base_fields.get('group').choices = user_groups
                context = {
                    'errors': 'Похожая задача уже существует.',
                    'form': form,
                }
                return render(request, self.template_name, context)
            else:
                fields = form.save(commit=False)
                fields.task_owner = self.request.user
                form.save()

                return redirect(self.success_url)
        return redirect(self.request.path)


class CreateNewTaskGroup(mixins.LoginRequiredMixin, CreateView):
    success_url = 'tasks_home'
    template_name = 'manager/new_group.html'

    model = TaskGroups
    form_class = CreateNewTaskGroupForm

    def post(self, request, *args, **kwargs):
        form = CreateNewTaskGroupForm(request.POST)
        if form.is_valid():
            fields = form.save(commit=False)
            user = self.request.user.pk
            all_user_groups = TaskGroups.objects.filter(creator_group=user).values_list('group_name', flat=True)
            # print(fields.group_name, all_user_groups)
            if fields.group_name in all_user_groups:
                form = CreateNewTaskGroupForm(request.POST)
                context = {
                    'group_name_error': f'Группа "{fields.group_name}" уже существует!',
                    'form': form,
                }
                return render(request, self.template_name, context)

            fields.creator_group = USER.objects.get(pk=self.request.user.pk)

            fields.save()
            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})


class TasksOfGroupView(mixins.LoginRequiredMixin, ListView):
    template_name = 'manager/tasks_in_group.html'
    context_object_name = 'grouped_tasks'

    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user.pk
        group = self.kwargs.get('group', None)
        groups_user_list = TaskGroups.objects.filter(creator_group=user).values('id', 'group_name')

        context['user_tasks_groups'] = groups_user_list
        context['grouped_tasks'] = Task.objects.filter(task_owner=user).filter(group=group)

        return context


class TaskHomeView(mixins.LoginRequiredMixin, ListView):
    # TODO: Написать пагинацию страниц по дате в таблице
    template_name = 'manager/tasks.html'
    redirect_field_name = 'tasks_home'
    context_object_name = 'tasks'

    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskHomeView, self).get_context_data(**kwargs)

        user = self.request.user.pk
        groups_user_list = TaskGroups.objects.filter(creator_group=user).values('id', 'group_name')

        context['title'] = 'Личные задачи'
        context['user_tasks_groups'] = groups_user_list

        return context

    def get_queryset(self):
        return Task.objects.filter(task_owner=self.request.user.pk)


class TaskDitail(mixins.LoginRequiredMixin, View):
    template_name = 'manager/task_ditail.html'
    context_object_name = 'tasks_home'
    form_class = CreateTaskForm

    def get(self, request, *args, **kwargs):
        user_groups = TaskGroups.objects.filter(creator_group=request.user.pk).values_list('id', 'group_name', )

        task = get_object_or_404(Task, pk=kwargs['pk'])
        formset = TasksFormSet(queryset=StagesOfExecuting.objects.filter(task=task))
        self.form_class.base_fields.get('group').choices = user_groups

        context = {
            'title': task.title_task,
            'form': self.form_class(instance=task),
            'formset': formset,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])

        form = self.form_class(request.POST, request.FILES, instance=task)
        formset = TasksFormSet(request.POST, request.FILES, )
        print("Status formset:", formset.is_valid(), "Status form:", form.is_valid())

        if form.is_valid() and formset.is_valid():
            fields = form.save(commit=False)
            fields.task_owner = self.request.user
            fields.save()

            fields_forms_set = formset.save(commit=False)
            for form in fields_forms_set:
                form.task = task
                form.save()
            formset.save()

            return redirect('task_group', kwargs['group'])

        context = {
            'title': f'Ошибка {task.title_task}',
            'form': self.form_class(instance=task),
            'formset': formset,
        }

        return render(self.request, self.template_name, context)
