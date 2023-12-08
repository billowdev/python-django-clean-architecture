# INIT DJANGO REST FRAMEWORK APPLICATION WITH CLEAN ARCHITECTURE AND MVC

## Reading List About Django

## Architecture Idea
- MVC
	- https://masteringdjango.com/django-tutorials/mastering-django-structure/
	- https://www.geeksforgeeks.org/mvc-framework-introduction/
	- https://developer.mozilla.org/en-US/docs/Glossary/MVC

- clean architecture
	- https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
	- https://dev.to/prodigy9/clean-architecture-1o9p

### This is a project stucture that build base on Clean architecture idea but not perfectly fit with the "core" business logic layer. because for In Django, views and serializers often involve interactions with the external frameworks

## Structure Tree
```
📦app-repo
 ┣ 📂core
 ┃ ┣ 📂settings
 ┃ ┃ ┣ 📂certificates
 ┃ ┃ ┃ ┣ 📜certificate.crt
 ┃ ┃ ┃ ┗ 📜certificate.key
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┣ 📜dev.py
 ┃ ┃ ┣ 📜environment.py
 ┃ ┃ ┗ 📜local.py
 ┃ ┣ 📂utils
 ┃ ┃ ┣ 📜base_view_utils.py
 ┃ ┃ ┗ 📜exception_utils.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜db.sqlite3
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂modules
 ┃ ┣ 📂order
 ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜serializers.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂user
 ┃ ┃ ┣ 📂migrations
 ┃ ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜filters.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜repositories.py
 ┃ ┃ ┣ 📜serializers.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.gitignore
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirements.txt
```
## I will show you the process for clean architecture on `User Module` but for `Oder modules` i just init it by no reason =..=

## PART 1: Starting django app

### 1. Create env

```bash
python -m venv ./.venv
```

- or using vs-code
```bash
CTRL + SHIFT + P -> Python: Create Environment -> Venv -> select the interpreter of python any version in your machine
```

### 2. Source to venv (linux - bash)

```bash
source ./.venv/Scripts/activate
```

### 3. install django and lib for Postgresql psycopg2

```bash
pip install Django
pip install psycopg2
```

### 4. create django app

```bash
django-admin startproject core
``` 

### 5. this step should have structure like this

```
📦application-repository
 ┣ 📂core
 ┃ ┣ 📂core
 ┃ ┣ ┣ 📜asgi.py
 ┃ ┣ ┣ 📜settings.py
 ┃ ┣ ┣ 📜urls.py
 ┃ ┣ ┣ 📜wsgi.py
 ┃ ┣ ┗ 📜__init__.py
 ┗ ┗ 📜manage.py
```

### 6. move core outside core like this

```
📦application-repository
 ┣ 📂core
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┗ 📜manage.py
```


### 7. pip freeze after install some package don't forget to pip freeze

```bash
pip freeze > requirements.txt
```
- will have requirements.txt file
```
📦application-repository
 ┣ 📂core
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📜manage.py
 ┗ 📜requirements.txt
```

### 8. preparing the config setting folder like this [อ่านเกี่ยวกับ wsgi และ asgi เพิ่มเติม](https://www.mindphp.com/%E0%B8%9A%E0%B8%97%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1/66-server-hosting/8569-what-is-asgi-server.html#:~:text=ASGI%20%E0%B8%84%E0%B8%B7%E0%B8%AD%E0%B8%AD%E0%B8%B0%E0%B9%84%E0%B8%A3%3F,%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B9%84%E0%B8%A1%E0%B9%88%20suport%20asynchronous%20Python)

#### 8.1 refactor to -> settings/base.py

```
📦application-repository
 ┣ 📂core
 ┃ ┣ 📂settings
 ┃ ┃ ┗ 📜base.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📜manage.py
 ┗ 📜requirements.txt
```

#### 8.2 add more files for each environment

```
📦application-repository
 ┣ 📂core
 ┃ ┣ 📂settings
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┣ 📜environment.py
 ┃ ┃ ┣ 📜dev.py
 ┃ ┃ ┣ 📜local.py
 ┃ ┃ ┣ 📜prod.py
 ┃ ┃ ┗ 📜uat.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📜manage.py
 ┗ 📜requirements.txt
```

#### 8.3 config wsgi.py, asgi.py and manage.py to use 'f' string import for easier to change env
    - 1. firstly must declare variable that contain present environment
    - APPLICATION_ENVIRONMENT is a env variable 
	- add this code to `environment.py` file
    
```py
import os
from importlib import import_module
## TODO: >>> CHANGE ENVIRONMENT ZONE
APPLICATION_ENVIRONMENT = 'local'
# APPLICATION_ENVIRONMENT = "dev"
## APPLICATION_ENVIRONMENT = "uat"

## !       STRIC ENVIRONMENT           !
## APPLICATION_ENVIRONMENT = "prod"
## !       STRIC ENVIRONMENT          !
## TODO: >>> CHANGE ENVIRONMENT ZONE

SETTINGS_BY_ENVIRONMENT = {
    'local': 'application.settings.local',
    'dev': 'application.settings.dev',
    'uat': 'application.settings.uat',
    'prod': 'application.settings.prod',
}

# TODO: for get the setting that base on current environment
def get_django_settings():
    DJANGO_SETTINGS_MODULE = SETTINGS_BY_ENVIRONMENT.get(APPLICATION_ENVIRONMENT)
    
    if DJANGO_SETTINGS_MODULE:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)
        settings_module = import_module(DJANGO_SETTINGS_MODULE)
        return settings_module
    else:
        print(f"Settings not found for '{APPLICATION_ENVIRONMENT}' environment.")
        return None
    
# TODO: For reuse function for get the setting base on current enviromnent 
# TODO: This function is call get_django_settings function 
# TODO: For get attribute of setting from argument that's setting_name base on current application environment 
# TODO: For the application environment you can setting on base setting
def get_setting(setting_name):
    settings_module = get_django_settings()
    if hasattr(settings_module, setting_name):
        return getattr(settings_module, setting_name)
    else:
        print(f"{setting_name} not found in the settings.")
```

#### 8.4 config manage.py to use setting base on present env by using f string
```py
"""Django's command-line utility for administrative tasks."""
import os
import sys
from core.settings.environment import APPLICATION_ENVIRONMENT

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'core.settings.{APPLICATION_ENVIRONMENT}')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

#### 8.5 wsgi.py old technology on python that WSGI (Web Server Gateway Interface) traditional web application with synchronous request-response cycles.

```py
from core.settings.environment import APPLICATION_ENVIRONMENT

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'core.settings.{APPLICATION_ENVIRONMENT}')

application = get_wsgi_application()
```

#### 8.6 asgi.py new technology on python that implement base on wsgi.py ASGI (Asynchronous Server Gateway Interface) real-time application that requires WebSocket support for handling asynchronous events.
- ASGI is well-suited for integrating with Celery when your application requires background task processing and distributed computing. [Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/)

```py
from core.settings.environment import APPLICATION_ENVIRONMENT

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'core.settings.{APPLICATION_ENVIRONMENT}')

application = get_asgi_application()
```


#### 8.7 install django restframework REF : [django-rest-framework](https://www.django-rest-framework.org/)

```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```

- added the rest_framework to settings

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
]
```

#### 8.8 install core header [django-cors-headers](https://pypi.org/project/django-cors-headers/)
```bash
pip install django-cors-headers
```
- setting base.py added the core header
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
	'corsheaders',
]
```

#### 8.9 generate certificated for db connection 
- [postgresql.org: Secure TCP/IP Connections with SSL](https://www.postgresql.org/docs/current/ssl-tcp.html)
- [virtuozzo.com: Establishing SSL Connection to PostgreSQL DB Server](https://www.virtuozzo.com/application-platform-docs/ssl-for-pgsql/)
- [django-ca.readthedocs.io: Managing certificates](https://django-ca.readthedocs.io/en/latest/cli/certs.html)

- create key : firstly mkdir core/settings/certificates`
```bash
openssl genrsa -out ./core/settings/certificates/certificate.key 4096
```

- create out csr
```bash
openssl req -new -key ./core/settings/certificates/certificate.key -out ./core/settings/certificates/certificate.crt -utf8
```

- after that full fill the info... but for this test i will put value as "TEST"
```bash
$ openssl req -new -key ./core/settings/certificates/certificate.key -out ./core/settings/certificates/certificate.crt -utf8
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:TH
State or Province Name (full name) [Some-State]:TEST
Locality Name (eg, city) []:TEST
Organization Name (eg, company) [Internet Widgits Pty Ltd]:TEST
Organizational Unit Name (eg, section) []:TEST
Common Name (e.g. server FQDN or YOUR name) []:TEST
Email Address []:TEST@gmail.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
```

#### 8.10 DJANGO SECRET KEY GENERATOR

- Access the Python Interactive Shell

```bash
python
```
- python sheel look like below
```bash
$ python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

- Import the get_random_secret_key()

```bash
from django.core.management.utils import get_random_secret_key
```

- Generate the Secret Key

```bash
print(get_random_secret_key())
```

- exit the python shell
```bash
exit()
```

- added the new secret key
```py
SECRET_KEY = django-insecure-YOUR_SECRET
```

#### 8.11 example core/settings/dev.py config (also for prod.py uat.py local.py will look like dev.py)

```py
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bkx+09#g4ei+q%(z%qm4e6pxwtcf_+j$35^a6dsn8vuf$ia$e@'

# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dev_db_name',
        'USER': 'dev_db_name',
        'PASSWORD': 'test',
        'HOST': 'HOST',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
            'sslcert': '/certificates/certificate.csr',
            'sslkey': '/certificates/certificate.csr',
            'sslrootcert': '/certificates/certificate.csr',
        }

    }
}

CSRF_TRUSTED_ORIGINS = []
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = []
CORS_ORIGIN_REGEX_WHITELIST = []
```

#### 8.12 example core/settings/local.py db sqlite
```py
from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p^jj6n*clr_o*(y0ieazv_=%xcj)igx5=0gliiqdyt(pnacz^*'

# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    },
}

CSRF_TRUSTED_ORIGINS = []
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = []
CORS_ORIGIN_REGEX_WHITELIST = []
```
 
<!-- TODO: PART 2 -->
## PART 2: Init Some App example for `modules/user`

### 2.1 start app fistly please mkdir `modules/`

#### 2.1.1 start user app

```
python manage.py startapp user
```

#### 2.1.2 move user to /modules/user

```
📦application-repository
 ┣ 📂core
 ┃ ┣ 📂settings
 ┃ ┃ ┣ 📂certificates
 ┃ ┃ ┃ ┣ 📜certificate.crt
 ┃ ┃ ┃ ┗ 📜certificate.key
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┣ 📜environment.py
 ┃ ┃ ┣ 📜dev.py
 ┃ ┃ ┗ 📜local.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜db.sqlite3
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂modules
 ┃ ┗ 📂user
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┗ 📜__init__.py
 ┣ 📜manage.py
 ┗ 📜requirements.txt
```

#### 2.1.3 modify app name in modules/user/apps.py from name = 'user' to name = 'modules.user'
```py
from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.user'
```

#### 2.1.4 installing user app to core/settings/base.py 

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
	'corsheaders',
    'modules.user'
]
```

### 2.2 add some model modules/user/model.py

- model.py
```py
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid

class UserManager(BaseUserManager):
	def create_user(self, username, password=None, role=None):
		...

	def create_superuser(self, username=None, password=None):
		...

class User(AbstractBaseUser, PermissionsMixin):
	...

```

- modules/user/admin.py

```py
from django.contrib import admin
from django.apps import apps
all_models = apps.get_app_config('user').get_models()

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        ...
        )
    
for model in all_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered as e:
        pass
```

### 2.3 added AUTH_USER_MODEL setting to core/settings/base.py

```
AUTH_USER_MODEL = 'user.User'
```

### 2.4 ! Importance must makemigrations user along with application

- make migrations application

```
python manage.py makemigrations 
```

- make migrations user

```
python manage.py makemigrations user
```

<!-- TODO: PART 3 -->
## PART 3: Init Some App example for `modules/order`

### 3.1 start user app

```
python manage.py startapp user
```

### 3.2 move user to /modules/order

```
📦application-repository
 ┣ 📂core
 ┃ ┣ 📂settings
 ┃ ┃ ┣ 📂certificates
 ┃ ┃ ┃ ┣ 📜certificate.crt
 ┃ ┃ ┃ ┗ 📜certificate.key
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┣ 📜environment.py
 ┃ ┃ ┣ 📜dev.py
 ┃ ┃ ┗ 📜local.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜db.sqlite3
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂modules
 ┃ ┗ 📂order
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┗ 📂user
 ┃ ┃ ┣ 📜admin.py
 ┃ ┃ ┣ 📜apps.py
 ┃ ┃ ┣ 📜models.py
 ┃ ┃ ┣ 📜tests.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┗ 📜__init__.py
 ┣ 📜manage.py
 ┗ 📜requirements.txt
```

### 3.3 modify app name in modules/order/apps.py from name = 'order' to name = 'modules.order'

```py
from django.apps import AppConfig
class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.order'
```

#### 3.4 installing user app to core/settings/base.py 

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
	'corsheaders',
    'modules.user',
    'modules.order'
]
```

### 3.5 add some model modules/order/model.py

```py
class Order(models.Model):
    ...

class OrderAssignee(models.Model):
    ...
	order = ...
	user = ...
```
### 3.6 migrate order
- makemigrations
```
python manage.py makemigrations order
```

- migrate
```
python manage.py migrate
```
<!-- TODO: PART 4 -->
## PART 4: MVC: urls, views, serializers, repository and models

### 4.1 System flow

- START
- 1. Urls: urls call the views
- 2. Views: the views call the serialziers for validate of the schema
- 3. Serializers: the serializers validate base on serializer type that custom serializer or model base
- 4. Views: in views after validate with serializers pass it to repository
- 5. Repository: repository do something with the model to save or process with database ex. CRUD process
-6 Views: Process the request or handle response success and error case
- END


### 4.2 core/utils/base_view_utils.py
```py
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import generics, status

class APIFormatException:
	def handle_format_exception(self, exception):
		try:
			if hasattr(exception, 'to_dict') and callable(exception.to_dict):
				error_data = exception.to_dict()
			else:
				error_data = str(exception)
		except Exception as e:
			error_data = str(e)
		return error_data

class APIResponseFormat:
	def handle_success_response(self, status_code="20000", message_code="SUCCESS", description="The request was successfully", response={}, http_status=status.HTTP_200_OK, pagination={}):
		"""_summary_
		Args:
			status_code (str, optional): _description_. Defaults to "20000".
			message_code (str, optional): _description_. Defaults to "Success".
			data (dict, optional): _description_. Defaults to {}.
			http_status (int, optional): _description_. Defaults to 200.

		Returns:
			_type_: _description_
		"""
		if pagination != {}:
			response = {
				"status_code": status_code,
				'message_code': message_code,
				"description": description,
				'data': response,
				'pagination':pagination
			}
		else:
			response = {
				"status_code": status_code,
				'message_code': message_code,
				"description": description,
				'data': response,
			}
		return JsonResponse(response, status=http_status)

	def handle_error_response(self, status_code="40000", message_code="BAD_REQUEST", description="Error response", response=None, http_status=status.HTTP_400_BAD_REQUEST, exception=None):
		try:
			error_data = self.handle_format_exception(exception)
		except:
			error_data = str(exception)
    
		response = {
				"status_code": status_code,
				"message_code": message_code,
				"description": description,
				"data": response,
				"error": error_data if exception else None
		}

		return JsonResponse(response, status=http_status)

class APIResponseView(APIView,  APIFormatException, APIResponseFormat):
	def __init__(self, **kwargs) -> None:
		super().__init__(**kwargs)
```

### 4.3 example user modules but we will driving from buttom to top
- 1. repositories
- 2. serialziers
- 3. views
- 4. urls

#### 4.3.1 Repo: modules/user/repositories.py

```py
from .models import User
from django.db import transaction
from django.contrib.auth.hashers import make_password

class UserRepository:
	def user_repo_get_one(self, resource_id):
		return User.objects.get(id=resource_id)

	def user_repo_get_all(self, sorting=None):
		if not sorting:
			return User.objects.all()
		else:
			return User.objects.all().order_by(sorting)

	@transaction.atomic
	def user_repo_create(self, user):
		with transaction.atomic():
			return User.objects.create(**user)

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
				instance.last_name = validated_data.get('last_name', instance.last_name)
				instance.password = validated_data.get('password', instance.password)
				instance.save()
				return instance
			except Exception as exception:
				raise exception

	@transaction.atomic
	def user_repo_remove(self, resource_id):
		with transaction.atomic():
			user = self.get_one(resource_id)
			user.delete()
			return True
```

#### 4.3.2 serialziers: modules/user/serialziers.py

```py
from rest_framework import serializers
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

class UserUpdateSerializer(serializers.ModelSerializer):
	username = serializers.CharField(max_length=100, required=False)
	password = serializers.CharField(max_length=100, required=False, write_only=False)
	first_name = serializers.CharField(required=False)
	last_name = serializers.CharField(required=False)
	role = serializers.CharField(required=False)
	is_active = serializers.BooleanField(required=False)
	class Meta:
		model = User
		fields = "__all__"

	def validate(self, attrs):
		return super().validate(attrs)
```

#### 4.3.3 views: modules/user/views.py

- composition-based -> flexibility and maintainability
- inheritance hierarchies -> If there's a clear "is-a" relationship and code reuse is a priority

- 1. create user

```py
from core.utils.base_view_utils import APIResponseView
from modules.user.repositories import UserRepository
from modules.user.serializers import UserSerializer

user_repository = UserRepository()

# Pros:
	# Loose coupling: Composition promotes loose coupling, making it easier to change or replace components without affecting the entire system.
	# Flexibility: With composition, you can easily switch the implementation of a component (such as changing the repository) without modifying the class itself.
# Cons:
	# More explicit dependencies: Composition might require more explicit management of dependencies compared to inheritance.
	# Potential code duplication: Depending on how the composition is implemented, you might end up with more boilerplate code.
 
class UserCreateView(APIResponseView):
	serializer_class = UserSerializer
	# ! composition (instance-based approach)
	repo = UserRepository()
	queryset = None
	def perform_create_logic(self, payload):
		serializer = self.serializer_class(data=payload)
		if serializer.is_valid(raise_exception=True):
			validated_data = serializer.validated_data
			instance =  self.repo.user_repo_create(validated_data)
			re_serialize = self.serializer_class(instance)
			response = re_serialize.data
			return response

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
```

- 2. get all user

- setting REST_FRAMEWORK for DjangoFilterBackend and pagination inside core/settings/base.py
```py
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend' ],
    'DEFAULT_PAGINATION_CLASS': ['rest_framework.pagination.LimitOffsetPagination'],
}
```

- 3. modify base_view_utils.py create util for pagination and filter

- import ListAPIView and pagination

```py
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
```

- create class pagination views [Django Pagination ListView Document](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/)

```py
class PaginationAPIResponse(ListAPIView, APIFormatException):
	def __init__(self, **kwargs) -> None:
		super().__init__(**kwargs)
```

- added the CustomPagination

```py
DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 10
class CustomPagination(PageNumberPagination, APIResponseView):
	page = DEFAULT_PAGE
	page_size = DEFAULT_PAGE_SIZE
	page_size_query_param = 'limit'
 
	def __init__(self, **kwargs) -> None:
		super().__init__(**kwargs)
  
	def get_paginated_response(self, data=None, status_code="20000", message_code="SUCCESS", message="The request process success"):
		try:
			response = {
				"status_code": status_code,
				"message_code": message_code,
				"message": message,
				"data": data,
				"pagination": {
					"links": {
						"next": self.get_next_link(),
						"previous": self.get_previous_link()
					},
					"total": self.page.paginator.count,
					"page": int(self.request.GET.get("page", DEFAULT_PAGE)),
					"page_size": int(self.request.GET.get("limit", self.page_size))
				}
				}
			return JsonResponse(response, status=status.HTTP_200_OK)
		except Exception as exception:
			response ={
				"status_code": "400001",
				"message_code": "Error",
				"message": "The request failed.",
				"data": [],
				"pagination": {
					"links": {
							"next": self.get_next_link(),
							"previous": self.get_previous_link()
						},
				"total": self.page.paginator.count,
				"page": int(self.request.GET.get("page", DEFAULT_PAGE)),
				"page_size": int(self.request.GET.get("limit", self.page_size))
				}
			}
			return JsonResponse(response, status=status.HTTP_200_OK)
```


- modules/user/filters.py

```py
from django_filters import FilterSet, CharFilter, DateTimeFilter
from datetime import datetime
from modules.user.models import User

class UserFilter(FilterSet):
	username = CharFilter(field_name="username", lookup_expr='iexact')
	email = CharFilter(field_name="email", lookup_expr='email')
	first_name = CharFilter(field_name="first_name", lookup_expr='icontains')
	last_name = CharFilter(field_name="last_name", lookup_expr='icontains')
	created_at = CharFilter(method='filter_created_at_iso')
	updated_at = CharFilter(method='filter_updated_at_iso')

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name',
			'created_at',
			'updated_at',
		]

	def filter_created_at_iso(self, queryset, name, value):
		from datetime import datetime
		iso_datetime = datetime.fromisoformat(value)
		return queryset.filter(created_at__date=iso_datetime.date())

	def filter_updated_at_iso(self, queryset, name, value):
		from datetime import datetime
		iso_datetime = datetime.fromisoformat(value)
		return queryset.filter(updated_at__date=iso_datetime.date())
```

- UserGetAllView modules/user/views.py
```py
# ! inheritance
#  Pros:
	# Code reuse: Inheritance allows you to reuse code from the parent classes (PaginationAPIResponse and UserRepository in this case).
	# A clear hierarchy: Inheritance can establish a clear hierarchy and express an "is-a" relationship between the subclass and its parents.
# Cons:
	# Tight coupling: Inheritance can create tight coupling between the subclass and its parent classes, making the code more rigid and harder to maintain.
	# Inheritance hierarchies can become complex and difficult to manage.
class UserGetAllView(PaginationAPIResponse, UserRepository):
	pagination_class = CustomPagination
	serializer_class = UserGetSerializer
	queryset = None
	filter_backends = [filters.SearchFilter, DjangoFilterBackend]
	filterset_class = UserFilter

	def perform_get_all_logic(self, sorting):
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
```

- UserGetOneView modules/user/views.py

```py
class UserGetOneView(APIResponseView, UserRepository):
	serializer_class = UserGetSerializer
	queryset = None
 
	def perform_get_one_logic(self, resource_id):
		self.queryset = self.user_repo_get_one(resource_id)
		if self.queryset:
			serializer = self.serializer_class(self.queryset, many=False)
			return serializer.data

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
```

- UserUpdateView modules/user/views.py

```py
class UserUpdateView(APIResponseView, UserRepository):
	serializer_class = UserUpdateSerializer
	queryset = None
 
	def perform_update_logic(self, resource_id, payload):
		instance = self.user_repo_get_one(resource_id)
		serializer = self.serializer_class(instance, data=payload)
		if serializer.is_valid(raise_exception=True):
			validated_data = serializer.validated_data
			updated = self.user_repo_update(instance, validated_data)
			re_serialize = self.serializer_class(updated)
			response = re_serialize.data
			return response

	def put(self, request, resource_id):
		try:
			request_data = request.data
			response = self.perform_update_logic(resource_id, request_data)
			if response:
				return self.handle_success_response(
					description=f"The update of a user was successful.",
					message_code="Success",
					status_code="20000",
					response=response
				)
			else:
				return self.handle_error_response(
					exception=None,
					status_code="40000",
					message_code="Bad Request",
					description = f"A user update one was failure.",
					)
		except Exception as exception:
			return self.handle_error_response(
				exception=exception,
				status_code="40000",
				message_code="Bad Request",
				description = f"A user update was failure.",
				)
```

- UserRemoveView modules/user/views.py

```py
class UserRemoveView(APIResponseView):
	serializer_class = UserGetSerializer
 
	def perform_remove_logic(self, resource_id):
		try:
			response = self.user_repo_remove(resource_id)
			return response
		except Exception as execption:
			raise execption

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
```

#### 4.3.4 urls: modules/user/urls.py

```py
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

```


<!-- TODO: PART 5 -->
## PART 5: Exceptions

- 1. repositories exception
	- 1.1 instance not found exception
- 2. serializer utilities
   - 2.1 custom validate exception custom serializer base
   - 2.2 handle default array returning from serializer validation model base
- 3. views: process request or perform logic exception
- 4. authentication exception
	- 4.1 Permission denied
	- 4.2 Invalid credential
	- 4.3 Token expired

### 5.1 Utilities exception `core/utils/exception_utils.py`

#### 5.1.1 Inheritance base Exception from `ApplicationException`

```py
class ApplicationException(Exception):
	def __init__(self, error_info, field=None, message="Something went wrong!", child_error=None, exception_type="AppException"):
		super().__init__(f"{error_info} Error: Field '{field}' - {message}")
		# TODO: Exception Type
		self.exception_type = exception_type
		# * The description for error_info argument
		# TODO: This can provide more technical and detailed information about the error.
		# TODO: It can include specifics like variable values, API codes, or any other relevant technical details.
		# TODO: The error_info is typically longer and more detailed than the message.
		self.error_info = error_info
		self.field = field
		# * The description for message argument
		# TODO: This should provide a concise, high-level description of the error.
		# TODO: It should convey what went wrong in a clear and user-friendly manner.
		# TODO: The message should be brief and to the point.
		self.message = message
		# TODO: child exception
		self.child_error = child_error if child_error is not None else []

	def to_dict(self):
		return {
			"exception_type": self.exception_type,
			"field": self.field,
			"message": self.message,
			"error": f"Error: {self.error_info}",
			"child_error": self.child_error,
		}

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return str(self.to_dict())
```



#### 5.1.2 `AppExceptionHelper`

```py
class AppExceptionHelper:
    # general exception as dictionary
	def format_exception(self, exception, exception_type, field=None):
		try:
			error_data = exception.to_dict()
		except AttributeError:
			error_data = str(exception)
		except Exception as exception:
			error_data = str(exception)
			
		new_child_error = []
		if isinstance(error_data, dict):
			if error_data.get('child_error') in (None, []):
				error_data.pop("child_error", None)
				new_child_error = [error_data]
			else:
				new_child_error = [error_data]
		else:
			new_child_error = [{
					"exception_type": exception_type,
					"field": field,
					"error": error_data,
					"message": "Something went wrong!"
				}]
		return new_child_error

	# TODO: to use with serializer validation error
	def format_serializer_validation_error(self, exception, error_info="serializers.ValidationError", exception_type="appValidationException"):
		error_dict = dict(exception.detail)
		child_errors = []

		for field, errors in error_dict.items():
			for error in errors:
				child_errors.append({
					"exception_type": exception_type,
					"field": field,
					"message": str(error),
					"error": error_info,
				})

		return child_errors

	def raise_serializer_validate_exception(self, field, exception, exception_type="AppValidationFailure"):
		try:
			new_child_error = self.format_exception(exception, exception.exception_type)
		except:
			new_child_error = str(exception)
			
		raise AppSerializerException(
			field=field,
			message=f"Failed to validate {field}.",
			exception_type=exception_type,
			error_info=f"Validation error occurred for '{field}'.",
			child_error=new_child_error
		)
  
	def raise_serializer_error(self, field, exception, exception_type="AppSerializerFailure"):
		try:
			child_errors = self.format_serializer_validation_error(exception=exception, exception_type=field)
		except:
			child_errors = f"field: {str(field)}, exception: {str(exception)}"
		raise AppSerializerException(
			field=field,
			message=f"{field} serialization encountered an error.",
			error_info=f"An error occurred while serializing {field} in {exception_type if exception_type else self.__class__.__name__}.",
			exception_type=exception_type if exception_type else self.__class__.__name__,
			child_error=child_errors
		)
  
	def raise_validate_required_field_error(self, field, exception_type=None):
		raise AppValidateException(
			field=field,
			message=f"{field.capitalize()} is required.",
			error_info="Missing Field",
			exception_type=exception_type
		)
  
	def raise_repository_instance_not_found_exception(self, field, exception_type="AppInstanceNotFound"):
		raise AppRepositoryException(
			field=field,
			message=f"Failed to retrieved a '{field}' due to a repository error.",
			error_info=f"The specified '{field}' instance was not found in the system.",
			exception_type=exception_type
		)

	def handle_char_validator(self, attr, field, max_length, exception_type="AppValidateException"):
		if attr:
			if len(attr) > max_length:
				raise AppValidateException(
					field=field,
					message=f"The provided value exceeds the maximum length of {str(max_length)} characters.",
					error_info=f"The length of the value '{field}' exceeded the maximum allowed limit of {max_length} characters.",
					exception_type=exception_type
				)
```

#### 5.1.3 Inheritance from ApplicationException Format for `repositories` exception `AppRepositoryException`

```py
class AppRepositoryException(ApplicationException, AppExceptionHelper):
	def __init__(self, field, message, child_error=None, error_info=None, exception_type="AppRepositoryException"):
		if child_error:
				try:
					child_error = self.format_exception(child_error, child_error.exception_type)
				except:
					child_error = str(child_error)
		if error_info:
			super().__init__(error_info, field, message, child_error, exception_type)
		else:
			super().__init__("Repository Exception", field, message, child_error, exception_type)
```

#### 5.1.4 Inheritance from ApplicationException Format for `serializers` exception `AppSerializerException` and `AppValidateException`

```py
class AppSerializerException(ApplicationException, AppExceptionHelper):
	def __init__(self, field, message, child_error=None, error_info=None, exception_type="AppSerializerException"):
		if child_error:
				try:
					child_error = self.format_exception(child_error, child_error.exception_type)
				except:
					child_error = str(child_error)
		if error_info:
			super().__init__(error_info, field, message, child_error, exception_type)
		else:
			super().__init__("Serializer Exception", field, message, child_error, exception_type)

class AppValidateException(ApplicationException, AppExceptionHelper):
	def __init__(self, field, message, child_error=None, error_info=None, exception_type="AppValidateException"):
		if child_error:
				try:
					child_error = self.format_exception(child_error, child_error.exception_type)
				except:
					child_error = str(child_error)
		if error_info:
			super().__init__(error_info, field, message, child_error, exception_type)
		else:
			super().__init__("Validate Exception", field, message, child_error, exception_type)
```

#### 5.1.5 Inheritance from ApplicationException Format for `views` exception `AppRequestException`

```py
class AppRequestException(ApplicationException, AppExceptionHelper):
	def __init__(self, field, message, child_error=None, error_info=None, exception_type="AppRequestException"):
		if child_error:
				try:
					child_error = self.format_exception(child_error, child_error.exception_type)
				except:
					child_error = str(child_error)
		if error_info:
			super().__init__(error_info, field, message, child_error, exception_type)
		else:
			super().__init__("Request Exception", field, message, child_error, exception_type)
```

#### 5.1.6 Inheritance from ApplicationException Format for `views` exception `AppAuthenticationException`

```py
class AppAuthenticationException(ApplicationException, AppExceptionHelper):
	def __init__(self, field, message, child_error=None, error_info=None, exception_type="AppAuthenticationException"):
		if child_error:
				try:
					child_error = self.format_exception(child_error, child_error.exception_type)
				except:
					child_error = str(child_error)
		if error_info:
			super().__init__(error_info, field, message, child_error, exception_type)
		else:
			super().__init__("Authentication Exception", field, message, child_error, exception_type)
```



### 5.2 Usage utilities exception `core/utils/exception_utils.

- start from repository, serializer, views

#### 5.2.1 user repository example exception usage

```py
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
			
```

- user repository example result of AppRepositoryException

```json
{
    "status_code": "40000",
    "message_code": "Bad Request",
    "description": "A user get all was failure.",
    "data": null,
    "error": {
        "exception_type": "AppRepositoryException",
        "field": "User",
        "message": "Retrieve User was process failed",
        "error": "Error: Retrieve all user was process failed",
        "child_error": "could not convert string to float: 'TEST_RAISE_EXCEPTION'"
    }
}
```

#### 5.2.2 user serializers example exception usage
```py
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
```

- example exception
```json
{
    "status_code": "40000",
    "message_code": "Bad Request",
    "description": "A user update was failure.",
    "data": null,
    "error": {
        "exception_type": "User",
        "field": "first_name",
        "message": "The provided value exceeds the maximum length of 100 characters.",
        "error": "Error: The length of the value 'first_name' exceeded the maximum allowed limit of 100 characters.",
        "child_error": []
    }
}
```

```json
{
    "status_code": "40000",
    "message_code": "Bad Request",
    "description": "A user update was failure.",
    "data": null,
    "error": {
        "exception_type": "User",
        "field": "role",
        "message": "Failed to validate role.",
        "error": "Error: Validation error occurred for 'role'.",
        "child_error": "validate user failed user role: client2 not matching in system"
    }
}
```

#### 5.2.3 user views example exception usage

```py
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
				error_info="The process create user was failed",
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
```

- example json response raise by AppRequestException
```json
{
    "status_code": "40000",
    "message_code": "Bad Request",
    "description": "A user creation failure.",
    "data": null,
    "error": {
        "exception_type": "AppRequestException",
        "field": "User",
        "message": "The process create user was filed",
        "error": "Error: The process create user was failed",
        "child_error": "could not convert string to float: 'TEST RAISE EXCEPTION'"
    }
}
```

- example json response raise by AppRequestException and have child serializer error

- test serializer
```py
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

	def validate(self, attrs):
		raise AppValidateException(
			field="User",
			message="User validate error",
			child_error="child_error",
			error_info="TEST RAISE SERIALIZER EXCEPTION",
			exception_type="exception_type"
		)
		return super().validate(attrs)
```
- response that error occurred from above test
```json
{
    "status_code": "40000",
    "message_code": "Bad Request",
    "description": "A user creation failure.",
    "data": null,
    "error": {
        "exception_type": "AppRequestException",
        "field": "User",
        "message": "The process create user was filed",
        "error": "Error: The process create user was failed",
        "child_error": [
            {
                "exception_type": "exception_type",
                "field": "User",
                "message": "User validate error",
                "error": "Error: TEST RAISE SERIALIZER EXCEPTION",
                "child_error": "child_error"
            }
        ]
    }
}
```

- rest part of example usage an exception in views 
```py
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
   
   
```