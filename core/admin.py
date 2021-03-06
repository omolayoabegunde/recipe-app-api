from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from core import models
from django.utils.translation import gettext as _  #required for multiple languages

class UserAdminClass(UserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields':('email',)}),
        (('Personal Info'), {'fields':('name',)}),
        (
            _('Permissions'),
            {
                'fields':('is_active','is_staff','is_superuser')
            }
        ),
        (_('Important dates'), {'fields':('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('email','password1','password2')
        }),
    )

admin.site.register(models.User, UserAdminClass)