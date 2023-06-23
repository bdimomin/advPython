from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('student/add/',views.studentAdd, name='student_add'),
    path('student/list/',views.studentList, name='student_list'),
    path('student/delete/<int:id>',views.studentDel,name="student_del"),
    path('student/edit/<int:id>',views.studentEdit,name="student_edit"),


    path('department/add/',views.departmentAdd,name='department_add'),
    path('department/list/',views.departmentList,name='department_list'),
    path('/department/delete/<int:id>',views.departmentDel,name='department_delete'),
    path('/department/edit/<int:id>',views.departmentEdit,name='department_edit')


]
