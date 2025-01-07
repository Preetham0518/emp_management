from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Department, Designation, Location, Employee, Skill
from django.forms import modelformset_factory


class CreateUserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=[('admin','admin'),('users','users')])
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','user_type']








class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['department_id','designation_name', 'designation_description', ]
        widgets = {
            'department_id': forms.Select(attrs={'class':'form-select'}),
            'designation_name':forms.TextInput(attrs={'class':'form-control'}),
            'designation_description': forms.Textarea(attrs={'class':'form-control','rows':4}),
        }
        labels = {
           'department_id':'Department',
           'designation_name':'Designation Name',
           'designation_descrition': 'Description',
        }
        
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields =['name','description']
    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['join_date','employee_no','name','contact','address','emp_start_date',
                  'emp_end_date','photo','status','department','designation','location']
        widgets = {
            'department' : forms.Select(attrs={'class':'form-select'}),
            'designation': forms.Select(attrs={'class':'form-select'}),
            'location': forms.Select(attrs={'class':'form-select'}),
            'address': forms.Textarea(attrs={'class':'form-control','rows':2}),
            'status': forms.Select(attrs={'class':'form-select'}),
            'join_date': forms.DateInput(attrs={'type':'date'}),
            'emp_start_date': forms.DateInput(attrs={'type':'date'}),
            'emp_end_date':forms.DateInput(attrs={'type':'date'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name', 'description']
        widgets = {
            'skill_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter skill name'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
        }
   


SkillFormSet = modelformset_factory(
    Skill,
    form =SkillForm,
    extra=1,
    can_delete=True
)

class UploadFileForm(forms.Form):
    file = forms.FileField()