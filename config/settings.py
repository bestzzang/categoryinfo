"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+++'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False    # 73. 배포시 True -> False 로 수정

ALLOWED_HOSTS = ['*']    # 73. 배포 후 내 도메인으로 수


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'haystack',      # 47. Search, getting started with Haystack.
    'django.contrib.sites',
    'allauth',       # 31. App(allauth) 추가
    'allauth.account',
    'allauth.socialaccount',
#    'allauth.socialaccount.providers.kakao',
#    'allauth.socialaccount.providers.naver',
#    'allauth.socialaccount.providers.daum',
    'allauth.socialaccount.providers.google',
#    'allauth.socialaccount.providers.facebook',
#    'allauth.socialaccount.providers.twitter',
    'member.apps.MemberConfig',   # 35. App(member) 추가
    'storages',  # S3 연
]

# 36. .member/forms.py 에서 coding을 회원가입 폼으로 사용하기 위한 설정 삽입
ACCOUNT_SIGNUP_FORM_CLASS = 'member.forms.SignupForm'


# 37. .config/settings.py에 mail send 설정 삽입
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '+++'
EMAIL_HOST_PASSWORD = '+++'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# 38. .member/urls.py 생성 생성 후 coding 복사




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 26. 템플릿 검색되도록 경로 추가
        'APP_DIRS': True,                               # 27. .shop 폴더에 templates/shop 디렉토리 생성하고 Views에 필요한 모든 html화일들 복사
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# 15. MEDIA_ROOT 옵션 설정
MEDIA_URL = '/media/'  # 16. MEDIA_ROOT 옵션 설정 추가

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 17. MEDIA_ROOT 옵션 설정 추가

# 18. .shop/admin.py 에서 관리자 페이지 coding 복사


# 48. .cofig/settings.py Haystack를 위한 coding 삽입
WHOOSH_INDEX=os.path.join(BASE_DIR, 'whoosh_index')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 49. shop 폴더에 search_indexes.py 파일 생성 후 coding 작성


# 32. .config/settings.py 에 allauth 설정 추가
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1


LOGIN_REDIRECT_URL = '/'

#django-allauth registraion settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =7
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

# 33. python manage.py migrate : 추가한 앱들의 데이터베이스 적용

# 회원가입 양식에 전화번호 추가하는 forms 작성
# 34. python manage.py startapp member
# 35. .config/settings.py INSTALLED_APPS에 App(member) 추가

# 69. .config/settings.py 에 S3 연동을 위한 설정 입력
AWS_ACCESS_KEY_ID = '+++'    # AWS.amazon IAM User name 의 Access key ID
AWS_SECRET_ACCESS_KEY = '+++'   # AWS.amazon IAM User name 의 Secret access key
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'categoryinfo'   # AWS.amazon IAM User name
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'

# 7. .config/asset_storage.py 화일 생성
