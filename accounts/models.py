from django.db import models
from .managers import  CustomUserManager
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
	name = models.CharField(_('name'), max_length=100)
	email = models.EmailField(_('email address'), unique=True)
	username = models.CharField(_('username'), unique=True, max_length=100)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['name', 'email']

	objects = CustomUserManager()


class Courses(models.Model):
    courseId = models.AutoField(primary_key=True)
    subjectName= models.CharField(max_length=255)

class Pupil(models.Model):
    pupilId = models.AutoField(primary_key=True)
    pupilName = models.CharField(max_length=255)
    std =models.CharField(max_length=50)
    posted_date = models.DateTimeField()
  