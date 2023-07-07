from django.db import models

# Create your models here.

class Authors(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    class Meta:
        db_table='author'
        ordering=['first_name']
        verbose_name_plural = "authors"

    def __str__ (self):
        return self.first_name +' '+ self.last_name




class Books(models.Model):
    name=models.CharField(max_length=255)
    isbn=models.CharField(max_length=50)
    author=models.ForeignKey(Authors,on_delete=models.CASCADE)

    class Meta:
        db_table='books'
        verbose_name_plural = "books"

    def __str__ (self):
        return self.name
        

