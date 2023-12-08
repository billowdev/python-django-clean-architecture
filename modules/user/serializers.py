from rest_framework import serializers
from core.utils.exception_utils import AppExceptionHelper, AppValidateException
from modules.user.models import User

class UserGetSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			"id", 
			"username", 
			"email", 
			'first_name', 
			'last_name', 
			'last_login', 
			'is_active', 
			'role', 
			'created_at', 
			'updated_at'
	  ]

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

	def validate(self, attrs):
		return super().validate(attrs)

class UserUpdateSerializer(serializers.ModelSerializer, AppExceptionHelper):
	username = serializers.CharField(max_length=100, required=False)
	password = serializers.CharField(max_length=100, required=False, write_only=False)
	first_name = serializers.CharField(required=False)
	last_name = serializers.CharField(required=False)
	role = serializers.CharField(required=False)
	is_active = serializers.BooleanField(required=False)
	class Meta:
		model = User
		fields = "__all__"
  
	def validate_role(self, role):
		if role not in ["admin", "client"]:
			self.raise_serializer_validate_exception(
				field="role",
				exception=f"validate user failed user role: {role} not matching in system",
				exception_type="User"
			)
	def validate(self, attrs):
		first_name = attrs.get("first_name")
		self.handle_char_validator(attr=first_name, field="first_name", max_length=100, exception_type=self.Meta.model.__name__)

		last_name = attrs.get("last_name")
		self.handle_char_validator(attr=last_name, field="last_name", max_length=100, exception_type=self.Meta.model.__name__)

		username = attrs.get("username")
		self.handle_char_validator(attr=username, field="username", max_length=64, exception_type=self.Meta.model.__name__)

		role = attrs.get("role")
		if role:
			self.validate_role(role)
		return super().validate(attrs)