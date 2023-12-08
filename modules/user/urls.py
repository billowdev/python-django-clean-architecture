from django.urls import include, path
from . import views

user_urls = [
    path('/', views.UserGetAllView.as_view(), name='/user_get_all'),
    path('/id/<str:resource_id>', views.UserGetOneView.as_view(), name='user_get_one'),
    path('/create', views.UserCreateView.as_view(), name='/user_create'),
    path('/update/<str:resource_id>', views.UserUpdateView.as_view(), name='user_update'),
    path('/remove/<str:resource_id>', views.UserRemoveView.as_view(), name='user_remove'),
]

user_api_urlpatterns = [
    path('users', include(user_urls))
]
