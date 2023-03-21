from django.contrib.auth import views as auth_views
from .views import RegistrationView, UserEditView
from django.urls import path

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('', auth_views.TemplateView.as_view(template_name='manager/base.html',
                                             extra_context={'title': 'Задачи'}),
         name='base_user'),
    path('login/', auth_views.LoginView.as_view(template_name='user_actions/login.html',
                                                extra_context={'title': 'Аутентификация'}),
         name='login'
         ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('profile/', UserEditView.as_view(), name='profile'),
]
