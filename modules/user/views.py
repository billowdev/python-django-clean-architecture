from core.utils.base_view_utils import APIResponseView, CustomPagination, PaginationAPIResponse
from core.utils.exception_utils import AppRequestException
from modules.user.repositories import UserRepository
from modules.user.serializers import UserSerializer, UserGetSerializer, UserUpdateSerializer
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend
from modules.user.filters import UserFilter

# user_repository = UserRepository()

# composition-based -> flexibility and maintainability
# inheritance hierarchies -> If there's a clear "is-a" relationship and code reuse is a priority

class UserCreateView(APIResponseView):
	serializer_class = UserSerializer
	# ! composition (instance-based approach)
	repo = UserRepository()
	queryset = None
	def perform_create_logic(self, payload):
		try:
			serializer = self.serializer_class(data=payload)
			if serializer.is_valid(raise_exception=True):
				validated_data = serializer.validated_data
				instance =  self.repo.user_repo_create(validated_data)
				re_serialize = self.serializer_class(instance)
				response = re_serialize.data
				return response
		except Exception as exception:
			raise AppRequestException(
				field="User",
				message="The process create user was filed",
				error_info="The process perform logic to create a user was failed",
				child_error=exception,
			)

	def post(self, request):
		try:
			request_data = request.data
			response = self.perform_create_logic(request_data)
			return self.handle_success_response(
				description=f"The creation of a user was successful.",
				message_code="Success",
				status_code="20000",
				response=response
			)
		except Exception as exception:
			return self.handle_error_response(
				exception=exception,
				status_code="40000",
				message_code="Bad Request",
				description = f"A user creation failure.",
				)

class UserGetAllView(PaginationAPIResponse, UserRepository):
	pagination_class = CustomPagination
	serializer_class = UserGetSerializer
	queryset = None
	filter_backends = [filters.SearchFilter, DjangoFilterBackend]
	filterset_class = UserFilter

	def perform_get_all_logic(self, sorting):
		try:
			self.queryset = self.user_repo_get_all(sorting)
			queryset = self.filter_queryset(self.get_queryset())
			page = self.paginate_queryset(queryset)
			if page is not None:
				serializer = self.serializer_class(page, many=True)
				response = self.get_paginated_response(data=serializer.data)
				return response
			else:
				serializer = self.get_serializer(queryset, many=True)
				return self.handle_success_response(
					description=f"The retrieve of a user was successful.",
					message_code="Success",
					status_code="20000",
					response=serializer.data
				)
		except Exception as exception:
			raise AppRequestException(
				field="User",
				message="The process get all user was filed",
				error_info="The process perform logic to get all user was failed",
				child_error=exception,
			)
   
	def get(self, request):
		try:
			sort = request.GET.get('sort')
			if sort != None:
				sorting = sort
			else:
				sorting = "-created_at"
			return self.perform_get_all_logic(sorting)
		except Exception as exception:
			return self.handle_error_response(
				exception=exception,
				status_code="40000",
				message_code="Bad Request",
				description = f"A user get all was failure.",
				)
   
class UserGetOneView(APIResponseView, UserRepository):
	serializer_class = UserGetSerializer
	queryset = None
 
	def perform_get_one_logic(self, resource_id):
		try:
			self.queryset = self.user_repo_get_one(resource_id)
			if self.queryset:
				serializer = self.serializer_class(self.queryset, many=False)
				return serializer.data
		except Exception as exception:
			raise AppRequestException(
				field="User",
				message="The process get one user was filed",
				error_info="The process perform logic to get one user was failed",
				child_error=exception,
			)
   
	def get(self, request, resource_id):
		try:
			response = self.perform_get_one_logic(resource_id)
			if response:
				return self.handle_success_response(
					description=f"The retrieve of a user was successful.",
					message_code="Success",
					status_code="20000",
					response=response
				)
			else:
				return self.handle_error_response(
					exception=None,
					status_code="40000",
					message_code="Bad Request",
					description = f"A user get one was failure.",
					)
		except Exception as exception:
			return self.handle_error_response(
				exception=exception,
				status_code="40000",
				message_code="Bad Request",
				description = f"A user get one was failure.",
				)
   
class UserUpdateView(APIResponseView, UserRepository):
	serializer_class = UserUpdateSerializer
	queryset = None
 
	def perform_update_logic(self, resource_id, payload):
		try:
			instance = self.user_repo_get_one(resource_id)
			serializer = self.serializer_class(instance, data=payload)
			if serializer.is_valid(raise_exception=True):
				validated_data = serializer.validated_data
				updated = self.user_repo_update(instance, validated_data)
				re_serialize = self.serializer_class(updated)
				response = re_serialize.data
				return response
		except Exception as exception:
			raise AppRequestException(
				field="User",
				message="The process update user was filed",
				error_info="The process perform logic to update user was failed",
				child_error=exception,
			)
   
	def put(self, request, resource_id):
		try:
			request_data = request.data
			response = self.perform_update_logic(resource_id, request_data)
			if response:
				return self.handle_success_response(
					description=f"The update of a user was successful.",
					message_code="SUCCESS",
					status_code="20000",
					response=response
				)
			else:
				return self.handle_error_response(
					exception=None,
					status_code="40000",
					message_code="BAD_REQUEST",
					description = f"A user update one was failure.",
					)
		except Exception as exception:
			return self.handle_error_response(
				exception=exception,
				status_code="40000",
				message_code="Bad Request",
				description = f"A user update was failure.",
				)
   
class UserRemoveView(APIResponseView):
	serializer_class = UserGetSerializer
 
	def perform_remove_logic(self, resource_id):
		try:
			response = self.user_repo_remove(resource_id)
			return response
		except Exception as exception:
			raise AppRequestException(
				field="User",
				message="The process update user was filed",
				error_info="The process perform logic to remove user was failed",
				child_error=exception,
			)

	def delete(self, request, resource_id):
		try:
			response = self.perform_remove_logic(resource_id)
			return self.handle_success_response(
					description=f"The delete a user was successful.",
					message_code="Success",
					status_code="20000",
					response=response
				)
		except Exception as exception:
			return self.handle_error_response(
				exception=exception,
				status_code="40000",
				message_code="Bad Request",
				description = f"A user delete was failure.",
				)
   
   