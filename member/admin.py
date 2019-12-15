from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# 43. .member 하위에 templates/member 디렉토리 생성 후 HTML들 복사