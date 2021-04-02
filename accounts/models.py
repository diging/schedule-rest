from django.db import models

# Create your models here.
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,
	PermissionsMixin
)
from django.db import models
from django.utils import timezone
import binascii
import os
from django.conf import settings

class UserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')


		user = self.model(
			email=self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
		)

		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, first_name, last_name, password):
		"""
		Creates and saves a superuser with the given email, date of
		birth and password.
		"""
		user = self.create_user(
			email,
			first_name,
			last_name,
			password
		)
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user


class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	first_name = models.CharField(max_length=40, null=True, blank=True)
	last_name = models.CharField(max_length=140, null=True, blank=True)
	date_joined = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.first_name

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		# Simplest possible answer: All admins are staff
		return self.is_superuser