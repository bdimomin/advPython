from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Department,Student
# Create your views here.

def index(request):
    return render(request,'index.html')

def department_add(request):
    if request.method=="POST":
        context = {'has_error': False}
        department_name=request.POST.get('department_name')
        Department.objects.create(department_name=department_name).save()

        if not context['has_error']:
            messages.success(request, '✅ Department Successfully Added!')
        
        else:
            messages.error(request, '⚠️ Department Failed to add!')
           
    return render(request,'students/department_add.html')

def department_list(request):
    departments=Department.objects.all()
    return render(request,'students/departments.html',{'departments':departments})

def student_add(request):
    departments= Department.objects.all()
    if request.method=="POST":
        context = {'has_error': False}
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        department=request.POST.get('department')
        Student.objects.create(name=name,email=email,phone=phone, department_id=department).save() 

        if not context['has_error']:
            messages.success(request, '✅ Student Successfully Added!')
        
        else:
            messages.error(request, '⚠️ Student Failed to add!')
            
    return render(request,'students/student_add.html',{'departments':departments})

def student_list(request):
    students=Student.objects.all()
    return render(request,'students/students.html',{'students':students})

def student_edit(request,id):
    if request.method=="GET":
        student=Student.objects.get(pk=id)
        department=Department.objects.get(pk=student.department_id)
        departments=Department.objects.all()
        context={'student':student,'department':department,'departments':departments}
        return render(request,'students/student_edit.html',context)
    else:
        context = {'has_error': False}
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        department=request.POST.get('department')
        Student.objects.create(name=name,email=email,phone=phone, department_id=department).save() 

        if not context['has_error']:
            messages.success(request, '✅ Student Successfully Updated!')
        
        else:
            messages.error(request, '⚠️ Student Data update Failed')
        return redirect('student_list')
    

def student_delete(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return redirect('student_list')
    




