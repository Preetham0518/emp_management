from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Department, Designation, Location, Employee, Skill, a2_general_organization_details_header
from django.forms import modelformset_factory


class CreateUserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=[('admin','admin'),('users','users')],required= False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




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
            'department' : forms.Select(attrs={'class':'form-select','id':'id_department'}),
            'designation': forms.Select(attrs={'class':'form-select','id':'id_designation'}),
            'location': forms.Select(attrs={'class':'form-select'}),
            'address': forms.Textarea(attrs={'class':'form-control,','rows':2}),
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
    

class GeneralOrganizationForm(forms.ModelForm):
    class Meta:
        model = a2_general_organization_details_header
        fields = [
            'organization_description_document_avaliable',
            'is_there_an_independant_quality_assurance_department',
            'is_production_planned_systamatically',
            'is_delivery_timed_planned_and_monitored',
            'production_planning_and_control_system',
            'is_inform_customer_of_delay',
            'is_work_instruction_for_production',
            'is_work_instruction_for_in_process_inspection',
            'is_work_instruction_for_final_inspection',
            'is_work_instruction_for_outgoing_goods_inspection',
            'is_inspection_work_result_documented',
            'one_time_delivery_compalince_last_or_current_year_percentage',
            'implemented_procedure_for_ensuring_non_conforming_products',
            'filled_personname',
            'filled_persondesignation',
            'filled_personsignature',
            'sendto_buyer_date',
        ]

    organization_description_document_avaliable = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')], 
        widget=forms.RadioSelect,
        required=True
    )
    is_there_an_independant_quality_assurance_department = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.RadioSelect,
        required=True
    )
    is_production_planned_systamatically = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.RadioSelect,
        required=True
    )
    is_delivery_timed_planned_and_monitored = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.RadioSelect,
        required=True
    )
    production_planning_and_control_system = forms.ChoiceField(
        choices=[('Work Procedure', 'Work Procedure'), ('Index Cards', 'Index Cards')],
        widget=forms.RadioSelect,
        required=True
    )
    is_inform_customer_of_delay = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.RadioSelect,
        required=True
    )
    is_work_instruction_for_production = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.RadioSelect,
        required=True
    )
    is_work_instruction_for_in_process_inspection = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.RadioSelect,
        required=True
    )
    is_work_instruction_for_final_inspection = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.RadioSelect,
        required=True
    )
    is_work_instruction_for_outgoing_goods_inspection = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.RadioSelect,
        required=True
    )
    is_inspection_work_result_documented = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.RadioSelect,
        required=True
    )
    one_time_delivery_compalince_last_or_current_year_percentage = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 1,
            'class': 'form-control',
        }),
        required=True
    )
    implemented_procedure_for_ensuring_non_conforming_products = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 1,
            'class': 'form-control',
        }),
        required=True
    )
    filled_personname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    filled_persondesignation = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    filled_personsignature = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False
    )
    sendto_buyer_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True
    )