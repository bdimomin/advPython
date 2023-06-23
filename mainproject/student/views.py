from django.shortcuts import render, redirect
from . forms import StudentForms, DepartmentForms
from . models import Student, Department

# Create your views here.

def index(request):
    return render(request,'student/index.html')

def studentList(request):
    students=Student.objects.all().order_by('id')
    return render(request,'student/studentlist.html',{'students':students})

def studentAdd(request):
    if request.method=="GET":
        form=StudentForms()
        return render(request,'student/studentAdd.html',{'form':form})
    else:
        form=StudentForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('student_list')

def studentDel(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect('student_list')


def studentEdit(request,id):
    if request.method=="GET":
        student=Student.objects.get(pk=id)
        form=StudentForms(instance=student)
        return render(request,'student/studentAdd.html',{'form':form})
    else:
         student=Student.objects.get(pk=id)
         form=StudentForms(request.POST,instance=student)
    if form.is_valid():
        form.save()
    return redirect('student_list')


def departmentAdd(request):
    if request.method=="GET":
        form= DepartmentForms()
        return render(request, 'student/departmentadd.html',{'form':form})
    else:
        data = DepartmentForms(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/department/list')
    
def departmentList(request):
    departments=Department.objects.all().order_by('id')
    return render(request,'student/departmentlist.html',{'departments':departments})

def departmentEdit(request,id):
    if request.method=="GET":
        department=Department.objects.get(pk=id)
        form=DepartmentForms(instance=department)
        return render(request,'student/departmentadd.html',{'form':form})
    else:
         department=Department.objects.get(pk=id)
         form=DepartmentForms(request.POST,instance=department)
    if form.is_valid():
        form.save()
    return redirect('department_list')

def departmentDel(request,id):
    department=Department.objects.get(pk=id)
    department.delete()
    return redirect('department_list')