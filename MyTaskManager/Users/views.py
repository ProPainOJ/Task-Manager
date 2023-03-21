from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import mixins
from django.views.generic import UpdateView

from Task_Manager.models import TaskGroups
from .forms import MyRegisterForm, UserEditForm
from django.views import View
import os

USER = get_user_model()


class RegistrationView(View):
    template_name = 'user_actions/registrations.html'

    def get(self, request):
        context = {
            'title': 'Регистрация',
            'form': MyRegisterForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = MyRegisterForm(request.POST)

        if form.is_valid():

            """ Проверка почты пользователя """
            if form.cleaned_data['email'] and USER.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template_name=self.template_name, context={
                    'title': 'Некорректные данные!',
                    'form': form,
                    'custom_error_message': 'Пользователь с данной почтой уже зарегистрирован!',
                })

            if form.cleaned_data['email']:
                email_user = USER.objects.filter(
                    email=form.cleaned_data['email'],
                )

            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            form.save()

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                TaskGroups.objects.create(creator_group=user,
                                          group_name="No Groups",
                                          description_group="Automatically generated standard group",
                                          )

                return redirect('base_user')
            else:
                return render(request, template_name=self.template_name, context={
                    'custom_error_message': 'Ошибка входа в личный кабинет : (',
                    'title': 'Ошибка регистрации',
                    'form': MyRegisterForm(request.POST),
                })
        else:
            return render(request, self.template_name, context={
                'title': 'Некорректные данные!',
                'form': form,
            })


class UserEditView(mixins.LoginRequiredMixin, UpdateView):
    success_url = 'profile'
    template_name = 'user_actions/edit_profile.html'

    model = USER
    form_class = UserEditForm

    def get(self, request, *args, **kwargs):
        instance = USER.objects.get(pk=request.user.pk)
        form = self.form_class(instance=instance)
        context = {
            'title': 'Личный профиль',
            "form": form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(USER, pk=request.user.pk)
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data.get('user_avatar'):
                user_avatars_path = os.path.join(os.getcwd(), f'media/user_{user.pk}/avatars/')
                if not os.path.exists(user_avatars_path):
                    os.mkdir(os.path.join(os.getcwd(), f'media/user_{user.pk}'))
                else:
                    for avatars in os.listdir(user_avatars_path):
                        os.remove(os.path.join(user_avatars_path, avatars))
                user.user_avatar = form.cleaned_data['user_avatar']

            if form.cleaned_data.get('email'):
                # TODO: Написать логику смены потчы.
                # user.email = form.cleaned_data['email']
                pass

            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            return redirect('base_user')

        else:
            return redirect('base_user')
