from django.db import models

class Department(models.Model):
    name= models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering=['name']
        db_table = "departments"

    def __str__(self):
        return self.name

class Student(models.Model):
    name= models.CharField(max_length=100,null=False,blank=False)
    email=models.EmailField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=15,null=False,blank=False)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        ordering=['name']
        db_table = "students"
        
    def __str__(self):
        return self.name

