from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('student/list/',views.students, name='student_list'),
    path('student/add/',views.studentAdd, name='student_add'),
    path('student/update/<int:id>/',views.student_update, name='student_update'),
    path('student/delete/<int:id>/',views.student_delete,name='student_delete'),

    path('department/list/',views.departments,name='department_list'),
    path('department/add/',views.departmentAdd, name='department_add'),
    path('department/update/<int:id>', views.department_update, name='department_update'),
    path('department/delete/<int:id>', views.department_delete, name='department_delete'),
]

