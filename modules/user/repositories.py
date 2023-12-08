from core.utils.exception_utils import AppExceptionHelper, AppRepositoryException
from .models import User
from django.db import transaction
from django.contrib.auth.hashers import make_password

class UserRepository(AppExceptionHelper):
	def user_repo_get_one(self, resource_id):
		try:
			return User.objects.get(id=resource_id)
		except User.DoesNotExist as exception:
			self.raise_repository_instance_not_found_exception(field="User", exception_type="UserNotFound")
		except Exception as exception:
			raise AppRepositoryException(
       			field="User", 
				message="Retrieve User one was process failed", 
				error_info=f"Retrieve User one where resource: {resource_id} was process failed",
				child_error=exception, 
    		)
   
	def user_repo_get_all(self, sorting=None):
		try:
			if not sorting:
				return User.objects.all()
			else:
				return User.objects.all().order_by(sorting)
		except User.DoesNotExist as exception:
			self.raise_repository_instance_not_found_exception(field="User", exception_type="UserNotFound")
		except Exception as exception:
			raise AppRepositoryException(
       			field="User", 
				message="Retrieve User was process failed", 
				error_info=f"Retrieve all user was process failed",
				child_error=exception, 
    		)
   
	@transaction.atomic
	def user_repo_create(self, user):
		with transaction.atomic():
			try:
				return User.objects.create(**user)
			except Exception as exception:
				raise AppRepositoryException(
					field="User", 
					message="Create User was process failed", 
					error_info=f"Create user was process failed",
					child_error=exception, 
				)
    
	@transaction.atomic
	def user_repo_update(self, instance, validated_data):
		with transaction.atomic():
			try:
				if 'password' in validated_data:
					validated_data['password'] = make_password(
						validated_data['password'], hasher='argon2')
				instance.username = validated_data.get('username', instance.username)
				instance.role = validated_data.get('role', instance.role)
				instance.first_name = validated_data.get('first_name', instance.first_name)
				# instance.is_active = common_util.common_util_normalize_boolean(validated_data.get('is_active', instance.is_active))
				instance.last_name = validated_data.get('last_name', instance.last_name)
				instance.password = validated_data.get('password', instance.password)
				instance.save()
				return instance
			except Exception as exception:
				raise AppRepositoryException(
					field="User", 
					message="Update User was process failed", 
					error_info=f"Update user was process failed",
					child_error=exception, 
				)

	@transaction.atomic
	def user_repo_remove(self, resource_id):
		with transaction.atomic():
			try:
				user = self.get_one(resource_id)
				user.delete()
				return True
			except User.DoesNotExist as exception:
				self.raise_repository_instance_not_found_exception(field="User", exception_type="UserNotFound")
			except Exception as exception:
				raise AppRepositoryException(
					field="User", 
					message="Delete User was process failed", 
					error_info=f"Delete User where resource: {resource_id} was process failed",
					child_error=exception, 
				)
			