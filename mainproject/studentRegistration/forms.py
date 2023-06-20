from django import forms 
from .models import Student, Department

class StudentForm(forms.ModelForm):

    class Meta:
        model=Student
        fields='__all__'


    def __init__(self,*args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['department'].empty_label="Select"


class DepartmentForm(forms.ModelForm):

    class Meta:
        model=Department
        fields='__all__'

    def __init__(self,*args, **kwargs):
        super(DepartmentForm,self).__init__(*args, **kwargs)

