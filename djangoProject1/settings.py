"""
Django settings for djangoProject1 project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b$mtx67gts3yehte4w@dshl=%vh0)fje9gfsx(-vmy5+e!hqb6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'polls',
    # 注册子应用
    # 子应用名.apps.子应用名首字母大写Config，或者直接写应用名称就可以
    # 'interfaces.apps.InterfacesConfig'
    'interfaces',
    'projects',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProject1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject1.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project',
        'USER': 'root',
        'PASSWORD': 'li123456',
        'HOST': '106.14.220.57',
        'PORT': '3307'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 定制drf框架的参数，覆盖rest_framework框架源码中的配置文件settings.py中对应的key-value
REST_FRAMEWORK = {
    # 定义解析器类，用于解析不同的前段参数类型，会自动根据请求头的content-type来解析参数
    # 无论前段端传递这三种参数的哪一种，都可以使用request.data来获取
    # 覆盖后按照这里的配置文件来设定
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        # 'rest_framework.parsers.FormParser',
        # 'rest_framework.parsers.MultiPartParser'
    ],
    # 定义渲染器类，用于返回不同的参数类型
    # 不同的参数可以根据前端请求的accept参数制定视图函数的的返回值的
    # 类型（视图函数必须使用from rest_framework.response import Response来进行返回）
    # 。rest_framework框架源码中的配置文件settings.py默认是下面2种，不指定自动识别可以覆盖指定
    # 如果前端不指定accept或者指定为application/json 那么以json数据返回
    # 如果指定accept为text/html（浏览器发起get请求时会自动指定），那么会以html数据返回
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # 当前搜索引擎配置全局生效
    # 'DEFAULT_FILTER_BACKENDS': ['rest_framework.filters.SearchFilter',rest_framework.filters.OrderingFilter],
    # Filtering，修改查询字符串参数的key，默认key是search
    'SEARCH_PARAM': 'search1',
    'ORDERING_PARAM': 'ordering1',
    # 指定分页引擎
    # 'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    # #自定义的分页引擎
    # 'DEFAULT_PAGINATION_CLASS': 'utils.pagination.PageNumberPagination',
    #
    # # 指定分页的每页的条数
    'PAGE_SIZE': 3,
    # 指定用于支持coreapi的schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 覆盖drf默认的认证
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #jwt token认证，顺序是先jwttoken-然后session，然后Basic
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication'
        # 支持账号密码进行认证
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    # 覆盖drf默认的授权
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
