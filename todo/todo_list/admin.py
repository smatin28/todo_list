from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from . import forms


class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser
    list_display = ['email', 'username']


# Register your models here.
admin.site.register(models.SchoolToDo)
admin.site.register(models.ExtracurricularToDo)
admin.site.register(models.OtherToDo)
admin.site.register(models.CustomUser, CustomUserAdmin)
