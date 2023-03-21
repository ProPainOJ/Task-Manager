from django.urls import path, include
from django.views.generic import TemplateView
from .views import TaskHomeView, TaskDitail, CreateNewTask, TasksOfGroupView, CreateNewTaskGroup

urlpatterns = [
    path('', TemplateView.as_view(template_name='manager/base.html',
                                  extra_context={'title': 'MᴛManager'}),
         name='Manager_home'),
    path('users/', include('Users.urls')),
    path('tasks/', TaskHomeView.as_view(), name='tasks_home'),
    path('tasks/new_group/', CreateNewTaskGroup.as_view(), name='new_group'),
    path('tasks/<int:group>/', TasksOfGroupView.as_view(), name='task_group'),
    path('tasks/new_task/', CreateNewTask.as_view(), name='new_task'),
    path('tasks/task<int:pk>ditail/', TaskDitail.as_view(), name='task_ditail'),
]
