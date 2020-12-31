from django.shortcuts import render, get_object_or_404
from django import forms
from django.shortcuts import redirect

from . import forms
from . import models
from rest_framework import viewsets
from . import serializers
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


def school_to_do_create(request):
    item = "School To-Do"
    form = forms.SchoolToDoForm()
    if request.method == 'POST':
        form = forms.SchoolToDoForm(request.POST)
        if form.is_valid():
            school_to_do = form.save(commit=False)
            school_to_do.user = request.user
            school_to_do.save()
            return redirect('todo_list:view_to_dos')
    return render(request, 'todo_list/form.html', {'form': form, 'item': item})


def extracurricular_to_do_create(request):
    item = "Extracurricular To-Do"
    form = forms.ExtracurricularToDoForm()
    if request.method == 'POST':
        form = forms.ExtracurricularToDoForm(request.POST)
        if form.is_valid():
            extracurricular_to_do = form.save(commit=False)
            extracurricular_to_do.user = request.user
            extracurricular_to_do.save()
            return redirect('todo_list:view_to_dos')
    return render(request, 'todo_list/form.html', {'form': form, 'item': item})


def other_to_do_create(request):
    item = "Other To-Do"
    form = forms.OtherToDoForm()
    if request.method == 'POST':
        form = forms.OtherToDoForm(request.POST)
        if form.is_valid():
            other_to_do = form.save(commit=False)
            other_to_do.user = request.user
            other_to_do.save()
            return redirect('todo_list:view_to_dos')
    return render(request, 'todo_list/form.html', {'form': form, 'item': item})


def view_to_dos(request):
    set_of_school_to_dos = models.SchoolToDo.objects.filter(user=request.user)
    set_of_extracurricular_to_dos = models.ExtracurricularToDo.objects.filter(user=request.user)
    set_of_other_to_dos = models.OtherToDo.objects.filter(user=request.user)
    return render(request, 'todo_list/view_todos.html',
                  {'school_to_dos': set_of_school_to_dos,
                   'extracurricular_to_dos': set_of_extracurricular_to_dos,
                   'other_to_dos': set_of_other_to_dos})


def school_to_do(request, id):
    school = get_object_or_404(models.SchoolToDo, id=id)
    return render(request, 'todo_list/school_to_do.html', {'school': school})


def extracurricular_to_do(request, id):
    extracurricular = get_object_or_404(models.ExtracurricularToDo, id=id)
    return render(request, 'todo_list/extracurricular_to_do.html',
                  {'extracurricular': extracurricular})


def other_to_do(request, id):
    other = get_object_or_404(models.OtherToDo, id=id)
    return render(request, 'todo_list/other_to_do.html', {'other': other})


def add_to_do(request):
    return render(request, 'todo_list/add_to_do.html')


def edit_school_to_do(request, id):
    item = get_object_or_404(models.SchoolToDo, id=id)
    form = forms.SchoolToDoForm(instance=item)
    if request.method == 'POST':
        form = forms.SchoolToDoForm(instance=item, data=request.POST)
        if form.is_valid():
            school_to_do = form.save()
            school_to_do.save()
            return redirect('todo_list:view_to_dos')
    return render(request, 'todo_list/form.html', {'form': form, 'item': item})


def edit_extracurricular_to_do(request, id):
    item = get_object_or_404(models.ExtracurricularToDo, id=id)
    form = forms.ExtracurricularToDoForm(instance=item)
    if request.method == 'POST':
        form = forms.ExtracurricularToDoForm(instance=item, data=request.POST)
        if form.is_valid():
            extracurricular_to_do = form.save()
            extracurricular_to_do.save()
            return redirect('todo_list:view_to_dos')
    return render(request, 'todo_list/form.html', {'form': form, 'item': item})


def edit_other_to_do(request, id):
    item = get_object_or_404(models.OtherToDo, id=id)
    form = forms.OtherToDoForm(instance=item)
    if request.method == 'POST':
        form = forms.OtherToDoForm(instance=item, data=request.POST)
        if form.is_valid():
            other_to_do = form.save()
            other_to_do.save()
            return redirect('todo_list:view_to_dos')
    return render(request, 'todo_list/form.html', {'form': form, 'item': item})


def delete_school_to_do(request, id):
    item = get_object_or_404(models.SchoolToDo, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('todo_list:view_to_dos')
    return render(request, 'todo_list/delete.html', {'item': item})


def delete_extracurricular_to_do(request, id):
    item = get_object_or_404(models.ExtracurricularToDo, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('todo_list:view_to_dos')
    return render(request, 'todo_list/delete.html', {'item': item})


def delete_other_to_do(request, id):
    item = get_object_or_404(models.OtherToDo, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('todo_list:view_to_dos')
    return render(request, 'todo_list/delete.html', {'item': item})


class SchoolToDoView(viewsets.ModelViewSet):
    queryset = models.SchoolToDo.objects.all()
    serializer_class = serializers.SchoolToDoSerializer


class ExtracurricularToDoView(viewsets.ModelViewSet):
    queryset = models.ExtracurricularToDo.objects.all()
    serializer_class = serializers.ExtracurricularToDoSerializer


class OtherToDoView(viewsets.ModelViewSet):
    queryset = models.OtherToDo.objects.all()
    serializer_class = serializers.OtherToDoSerializer


class SignUpView(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
