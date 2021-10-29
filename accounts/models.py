from django.db import models
from .managers import  CustomUserManager
from django.utils import timezone
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
    description= models.CharField(max_length=1000)
    posted_date = models.DateTimeField(default=timezone.now)
	

class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	notes = models.TextField(max_length=1000)

	def __str__(self):
		return self.first_name