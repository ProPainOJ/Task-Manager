from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

_MAX_SIZE = 1920

categories_and_paths = {
    'avatar': '/avatars/',
    'video': '/videos/',
    'photo': '/photos/',
}


def user_directory_path(instance, filename):
    """ file will be uploaded to MEDIA_ROOT/user_<id>/category/filename> """
    return f'user_{instance.pk}/{categories_and_paths[instance.category]}/{filename}'


class MyUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = models.CharField(_('username'), max_length=150, blank=False, )

    email = models.EmailField(_('email address'), unique=True, blank=False,
                              error_messages={"unique": _("A user with that email already exists."), }, )

    category = 'avatar'
    user_avatar = models.ImageField(verbose_name='Фотография пользователя.',
                                    help_text='Путь файла: MEDIA_ROOT/user_id/category/filename',
                                    upload_to=user_directory_path,
                                    default='default_avatar/default.png',
                                    null=True, blank=True,
                                    max_length=250,
                                    )

    def save(self, *args, **kwargs):
        """ Изменение и сохранение размера user_avatar на _MAX_SIZE с пропорциями """
        super(MyUser, self).save(*args, **kwargs)
        filepath = self.user_avatar.path
        width = self.user_avatar.width
        height = self.user_avatar.height
        max_size = max(width, height)
        if max_size > _MAX_SIZE:
            image = Image.open(filepath)
            image = image.resize(
                (round(width / max_size * _MAX_SIZE),
                 round(height / max_size * _MAX_SIZE)),
                Image.ANTIALIAS
            )
            image.save(filepath)

    def __str__(self):
        if self.username:
            return f'{self.username}, {self.email}'
        else:
            return f'{self.email}'
