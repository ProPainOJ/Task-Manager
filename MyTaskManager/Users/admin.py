from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import MyUser


@admin.register(MyUser)
class UserAdmin(ModelAdmin):
    list_display = ('id', 'username', 'email',)
    list_display_links = ('username', 'email',)
    list_filter = ('id', 'is_active', 'is_staff', 'is_superuser',)
    actions_on_bottom = True
    actions_on_top = False
    readonly_fields = ('password',)
    search_fields = ('id', 'username', 'email')
    search_help_text = 'Поля для поиска: ID, имя пользователя, адрес электронной почты.'

    fieldsets = (
        ('Основная информацмя', {
            'fields': ('username', 'password', 'first_name', 'last_name', 'email',)
        }),
        ('Персонализация', {
            'fields': ('date_joined', 'last_login', 'user_avatar')
        }),
        ('Статусы', {
            'fields': ('is_staff', 'is_superuser', 'is_active')
        }),
    )

    # def get_form(self, request, obj=None, change=False, **kwargs):
    # """ Способ поменять verbose_name при получении формы """
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['user_avatar'].label = 'Фотография пользователя.'
    #     return form
