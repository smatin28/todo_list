from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SchoolToDoForm(forms.ModelForm):
    class Meta:
        model = models.SchoolToDo
        fields = ['title', 'description', 'due_date', 'course', 'category', ]


class ExtracurricularToDoForm(forms.ModelForm):
    class Meta:
        model = models.ExtracurricularToDo
        fields = ['title', 'description', 'due_date', 'category', ]


class OtherToDoForm(forms.ModelForm):
    class Meta:
        model = models.OtherToDo
        fields = ['title', 'description', 'due_date', 'category', ]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.CustomUser
        fields = ('username', 'email')
