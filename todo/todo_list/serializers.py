from rest_framework import serializers

from . import models


class SchoolToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SchoolToDo
        fields = ('title', 'description', 'due_date', 'course', 'category', )


class ExtracurricularToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExtracurricularToDo
        fields = ('title', 'description', 'due_date', 'category', )


class OtherToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtherToDo
        fields = ('title', 'description', 'due_date', 'category', )
