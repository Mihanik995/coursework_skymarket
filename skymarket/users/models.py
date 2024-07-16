from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, verbose_name=_('first name'))
    last_name = models.CharField(max_length=50, verbose_name=_('last name'))
    phone = PhoneNumberField(verbose_name=_('phone number'))
    email = models.EmailField(verbose_name=_('e-mail'))
    role = models.CharField(max_length=30, choices=[(UserRoles.USER, 'User'), (UserRoles.ADMIN, 'Administrator')]
                            , verbose_name=_('role'))
    image = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name=_('avatar'))

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN  #

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()
