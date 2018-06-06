from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(db_index=True, max_length=64, verbose_name='Phone', null=True, blank=True)

    # class Meta:
    #     app_label = 'app_auth'
    #     db_table = "app_user"