from django.urls import path, include

from . import views
from rest_framework import routers

app_name = "todo_list"

router = routers.DefaultRouter()
router.register('school_to_do', views.SchoolToDoView)
router.register('extracurricular_to_do', views.ExtracurricularToDoView)
router.register('other_to_do', views.OtherToDoView)

urlpatterns = [
    path('school_to_do_create/', views.school_to_do_create,
         name="school_to_do_create"),
    path('extracurricular_to_do_create/', views.extracurricular_to_do_create,
         name="extracurricular_to_do_create"),
    path('other_to_do_create/', views.other_to_do_create,
         name="other_to_do_create"),
    path('todos/', views.view_to_dos, name="view_to_dos"),
    path('add_to_do/', views.add_to_do, name="add_to_do"),
    path('<int:id>/school_to_do', views.school_to_do,
         name="school_to_do"),
    path('<int:id>/extracurricular_to_do', views.extracurricular_to_do,
         name="extracurricular_to_do"),
    path('<int:id>/other_to_do', views.other_to_do, name="other_to_do"),
    path('<int:id>/edit_school_to_do', views.edit_school_to_do,
         name="edit_school_to_do"),
    path('<int:id>/edit_extracurricular_to_do',
         views.edit_extracurricular_to_do, name="edit_extracurricular_to_do"),
    path('<int:id>/edit_other_to_do', views.edit_other_to_do,
         name="edit_other_to_do"),
    path('<int:id>/delete_school_to_do', views.delete_school_to_do,
         name="delete_school_to_do"),
    path('<int:id>/delete_extracurricular_to_do',
         views.delete_extracurricular_to_do,
         name="delete_extracurricular_to_do"),
    path('<int:id>/delete_other_to_do', views.delete_other_to_do,
         name="delete_other_to_do"),
    path('api/', include(router.urls)),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
