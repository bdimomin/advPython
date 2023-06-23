from django import forms
from . models import Student, Department

class StudentForms(forms.ModelForm):
    
    class Meta:
        model=Student
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(StudentForms,self).__init__(*args, **kwargs)
        self.fields['department'].empty_label="Select"


class DepartmentForms(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(DepartmentForms,self).__init__(*args, **kwargs)
     