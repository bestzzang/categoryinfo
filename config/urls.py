"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('search/', include('haystack.urls')),
    path('', include('shop.urls')),
    path('member/', include('member.urls')),
]



# 23. 프로젝트 최상위에 templates 디렉토리 생성
# 24. .templates 폴더에 base.html 화일 만들고 coding 복사


# 71. .config/urls.py 수정 삭제
# 29. .config/urls.py static을 사용해서 MEDIA_URL에 해당하는 주소를 가진 요청에 대해서는 MEDIA_ROOT에서 찾아서 응답하도록 urlpatterns에 추가하는 구문. 이 구문은 디버그 모드가 True일 때만 동작함.
#from django.conf.urls.static import static
#from django.conf import settings

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 30. pip install django-allauth : 소셜로그인 추가하기
# 31. .config/settings.py INSTALLED_APPS에 App(allauth) 추가