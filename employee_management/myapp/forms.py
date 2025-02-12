from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Department, Designation, Location, Employee, Skill, a2_general_organization_details_header, b10_material_inspection_testing_equipment_services_questionnaire_details_header
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
    
    
class b10Form(forms.ModelForm):
    class Meta:
        model = b10_material_inspection_testing_equipment_services_questionnaire_details_header
        fields = [
            'liquid_penetrant_inspection','liquid_penetrant_inspection_means','magnetic_particle_test',
            'magnetic_particle_test_means','magnetic_particle_test_equipment','ultrasonic_test',
            'ultrasonic_test_equipment','radio_graphic_test_with_xray_tube','radio_graphic_test_with_xray_tube_equipment',
            'radio_graphic_test_with_gama_radiation','radio_graphic_test_with_gama_radiation_elements',
            'pressure_test','pressure_test_type','leak_test','leak_test_type','identification_test',
            'identification_test_type','diamensional_check_mannual','diamensional_check_mannual_equipment',
            'diamensional_check','three_d_measuring_machine','tension_test','hot_tension_test_temp','notched_bar_impact_bending_test',
            'notched_bar_impact_bending_test_temp_from','notched_bar_impact_bending_test_temp_to','iso_v_specimen',
            'charpy_v_notch_specimen','hardness_test','brinell','vickers','rockwell','other_mechanical_test','other_mechanical_test_detail',
            'macro','micro','intergrannular_corrosion','wet_analysis','spectro_scopic_analysis','sand_analysis_for_foundry_sand',
            'other_chemical_analysis_method','other_chemical_analysis_method_detail','is_regular_checking_of_measuring_equipment',
            'is_records_traceable','is_samples_marked_with_heat_no','is_records_traceable_to_heat_no','is_part_marked_with_heat_no',
            'is_heat_no_traceable_to_furnace_change','is_prototype_parts_checked_internally','prototype_parts_checking_method',
            'is_parts_checked_by_random_sampling','random_sampling_checking_method','is_welding_procedure_qualified',
            'welding_procedure_qualified_standard','is_welders_qualified','welders_qualified_standard','is_defects_checked_prior_to_welding',
            'certiticate_file','defective_material_identification_method','reject_rework_rate','foundary_forge_shop_intern_reject_rework_rate',
            'foundary_forge_shop_extern_reject_rework_rate','machining_reject_rework_rate','finished_product_reject_rework_rate',
            'sendto_buyer_date','filled_personname','filled_persondesignation','filled_personsignature',
        ]
        
    liquid_penetrant_inspection = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    liquid_penetrant_inspection_means = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    magnetic_particle_test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    magnetic_particle_test_means = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    magnetic_particle_test_equipment = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    ultrasonic_test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    ultrasonic_test_equipment = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    radio_graphic_test_with_xray_tube = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    radio_graphic_test_with_xray_tube_equipment = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    radio_graphic_test_with_gama_radiation = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    radio_graphic_test_with_gama_radiation_elements = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    pressure_test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    pressure_test_type = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    leak_test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    leak_test_type = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    identification_test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    identification_test_type = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    diamensional_check_mannual = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    diamensional_check_mannual_equipment = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    diamensional_check = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    three_d_measuring_machine = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect,
        required=False,
    )
    tension_test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    hot_tension_test_temp = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': 'OCelsius'})
    )
    notched_bar_impact_bending_test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    iso_v_specimen = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    charpy_v_notch_specimen = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    hardness_test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    brinell = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    vickers = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    rockwell = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    other_mechanical_test = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    other_mechanical_test_detail = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    macro = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    micro = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    intergrannular_corrosion = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    wet_analysis = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    spectro_scopic_analysis =forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    sand_analysis_for_foundry_sand = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    other_chemical_analysis_method = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )
    other_chemical_analysis_method_detail = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    is_regular_checking_of_measuring_equipment = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    is_records_traceable = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    is_samples_marked_with_heat_no = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    is_records_traceable_to_heat_no = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    is_part_marked_with_heat_no = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    is_heat_no_traceable_to_furnace_change = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    is_prototype_parts_checked_internally = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    prototype_parts_checking_method = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    is_parts_checked_by_random_sampling = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    random_sampling_checking_method = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    is_welding_procedure_qualified = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    welding_procedure_qualified_standard = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    is_welders_qualified = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    welders_qualified_standard = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'value': '?'})
    )
    is_defects_checked_prior_to_welding = forms.ChoiceField(
        choices=[('Yes','Yes'),('No','No')],
        widget=forms.RadioSelect(),
        required=False,
    )
    certiticate_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        required=False
    )
    defective_material_identification_method = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    reject_rework_rate = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    foundary_forge_shop_intern_reject_rework_rate = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    foundary_forge_shop_extern_reject_rework_rate = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    machining_reject_rework_rate = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    finished_product_reject_rework_rate = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    sendto_buyer_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True
    )
    filled_personname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    filled_persondesignation = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    filled_personsignature = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    
    