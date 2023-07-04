from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('department_add/',views.department_add,name="department_add"),
    path('departments/',views.department_list,name='department_list'),
    path('student_add/',views.student_add, name='student_add'),
    path('students/',views.student_list, name='student_list'),
    path('student/edit/<int:id>',views.student_edit, name='student_edit'),
    path('student/del/<int:id>',views.student_delete,name="student_delete")
]
