from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, RegistForm


User = get_user_model()


class CustomizeUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = RegistForm

    list_display = ('username', 'circle', 'is_staff')

    fieldsets = (
        ('ユーザ情報', {'fields': ('username', 'email', 'password', 'picture', 'website', 'circle', 'circle_info')}),
        ('パーミッション', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        ('ユーザ情報', {
            'fields': ('username', 'email', 'password', 'confirm_password', 'website', 'circle', 'circle_info')
        }),
    )


admin.site.register(User, CustomizeUserAdmin)
