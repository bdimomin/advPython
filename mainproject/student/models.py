from django.db import models

class Department(models.Model):
    department=models.CharField(max_length=100,null=False, blank=False)

    class Meta:
        ordering=['department']
        db_table='departments'

    def __str__(self):
        return self.department

class Student(models.Model):
    name = models.CharField(max_length=50,null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email= models.EmailField(max_length=50)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table='students'

    def __str__(self):
        return self.name
