from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class ToDoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(_("Date (YYYY-MM-DD)"), blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
        ordering = ['due_date']

    def __str__(self):
        return self.title


class SchoolToDo(ToDoItem):
    course = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)


class ExtracurricularToDo(ToDoItem):
    category = models.CharField(max_length=255, blank=True)


class OtherToDo(ToDoItem):
    category = models.CharField(max_length=255, blank=True)
