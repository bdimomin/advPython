from django.shortcuts import render, redirect
from .forms import StudentForm, DepartmentForm
from . models import Student, Department

def index(request):
    return render(request,'student/index.html')

def students(request):
    content=Student.objects.all().order_by('id')
    return render(request,'student/students.html',{'content':content})


def studentAdd(request):
    if request.method=="GET":
        form= StudentForm()
        return render(request,'student/studentadd.html',{'form':form})
    else:
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/student/list/')


def student_update(request,id):
    if request.method=="GET":
        student= Student.objects.get(pk=id)
        form=StudentForm(instance=student)
        return render(request,'student/studentadd.html',{'form':form})
    else:
        student=Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=student)
    if form.is_valid():
        form.save()
    return redirect('student_list')

def student_delete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect('student_list')


def departments(request):
    content = Department.objects.all().order_by('id')
    return render(request,'student/departments.html',{'content':content})


def departmentAdd(request):
    if request.method=="GET":
        department=DepartmentForm()
        return render(request,'student/departmentadd.html',{'department':department})
    else:
        department=DepartmentForm(request.POST)
        if department.is_valid():
            department.save()
        return redirect('/department/list/')
    
def department_update(request,id):
    if request.method=="GET":
        dep=Department.objects.get(pk=id)
        department=DepartmentForm(instance=dep)
        return render(request,'student/departmentadd.html',{'department':department})
    else:
        department=Department.objects.get(pk=id)
        form=DepartmentForm(request.POST, instance=department)

    if form.is_valid():
        form.save()
    return redirect('department_list')

def department_delete(request,id):
    department=Department.objects.get(pk=id)
    department.delete()
    return redirect('department_list')




