from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid

class UserManager(BaseUserManager):
	def create_user(self, username, password=None, role=None):
		if username is None:
			raise TypeError('Users should have a username')
		if role is None:
			raise TypeError('Users should have a role')
		
		user = self.model(username=username)
		user.role = role
		user.set_password(password)

		user.save()
		return user

	def create_superuser(self, username=None, password=None):
		if password is None:
			raise TypeError('Password should not be none')
		
		user = self.create_user(username, password, 'admin')
		user.is_superuser = True
		user.is_staff = True
		user.is_active = True
		user.save()
		return user

class User(AbstractBaseUser, PermissionsMixin):
	class Meta:
		db_table = "users"
  
	USER_ROLE = [('admin', 'Admin'), ('client', 'Client')]
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	username = models.CharField(max_length=255, unique=True, null=False, blank=False)
	email = models.CharField(max_length=255, unique=True, null=False, blank=False)
	password = models.CharField(max_length=255, null=False, blank=False)
	first_name = models.CharField(max_length=255, null=True, blank=True)
	last_name = models.CharField(max_length=255, null=True, blank=True)
	role = models.CharField(max_length=20, default='client', choices=USER_ROLE, null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
	objects = UserManager()

	def __str__(self):
		return f"{self.username}"
	
	def to_dict(self):
		return {
			'id': str(self.id),
			'username': self.username,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'role': self.role,
			'created_at': self.created_at.isoformat(),
			'updated_at': self.updated_at.isoformat(),
			'is_active': self.is_active,
			'is_staff': self.is_staff,
		}