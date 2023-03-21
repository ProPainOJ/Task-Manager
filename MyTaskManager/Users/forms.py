from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

USER = get_user_model()


class MyRegisterForm(UserCreationForm):
    """ Форма регистрации нового пользователя """

    username = forms.CharField(label='Имя пользователя',
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label='Почта',
                             required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = USER
        fields = ['email', 'username', 'password1', 'password2']


class MyUserEditForm(forms.ModelForm):
    """ Форма на основе модели пользователя для её редактирования """

    class Meta(object):
        model = USER
        fields = '__all__'


class UserEditForm(forms.ModelForm):
    """ Форма для редактирования профеля пользователя """

    class Meta:
        model = USER
        fields = ['username', 'first_name', 'last_name', 'user_avatar', ]

    username = forms.CharField(label='username',
                               max_length=50,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'edit-form'}),
                               )

    first_name = forms.CharField(label="Имя",
                                 max_length=25,
                                 required=False,
                                 widget=forms.TextInput(attrs={'class': 'edit-form'}),
                                 )

    last_name = forms.CharField(label="Фамилия",
                                max_length=40,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'edit-form'}),
                                )

    user_avatar = forms.ImageField(label='Загрузка нового фото профеля.',
                                   required=False,
                                   widget=forms.FileInput,
                                   )

    # email = forms.EmailField(label="email address",
    #                          widget=forms.TextInput(attrs={'class': 'edit-form'}), )
