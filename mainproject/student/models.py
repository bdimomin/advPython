from django.db import models


# Create your models here.

class Department(models.Model):
    department_name=models.CharField(max_length=255)

    class Meta:
        db_table='department'

    def __str__ (self):
        return self.department_name
    
class Student(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        db_table='student'

    def __str__ (self):
        return self.name
