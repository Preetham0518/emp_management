from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,related_name='%(class)s_created',on_delete=models.SET_NULL,null=True,
                blank=True)
    updated_by = models.ForeignKey(User,related_name='%(class)s_updated',on_delete=models.SET_NULL,null=True,
                                blank=True)
    class Meta:
        abstract = True
        
class Department(TimeStampedModel):
    department_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Designation(TimeStampedModel):
    designation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation_name = models.CharField(max_length=100)
    designation_description = models.TextField()
    
    def __str__(self):
        return self.designation_name

class Location(TimeStampedModel):
    location_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Employee(TimeStampedModel):
    STATUS_CHOICES = [
        ('active','Active'),
        ('inactive', 'Inactive'),
        ('terminated','Terminated'),
    ]
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    join_date = models.DateField()
    employee_no = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    emp_start_date = models.DateField()
    emp_end_date = models.DateField(null=True,blank=True)
    photo = models.ImageField(upload_to='employee_photos/',null=True,blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='active')
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Skill(TimeStampedModel):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="skills")
    skill_name = models.CharField(max_length=25)
    description = models.TextField()
    
    def __str__(self):
        return self.skill_name





class a2_general_organization_details_header(models.Model):
    general_organization_details_header_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(null=True, blank=True)

    description_document_avaliable_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )

    organization_description_document_avaliable = models.CharField(max_length=10, null=True, blank=True,
                                                                   choices=description_document_avaliable_CHOICES,
                                                                   default='')
    organization_description_document_file = models.FileField(null=True, blank=True, upload_to='audit_files')
    independant_quality_assurance_department_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    is_there_an_independant_quality_assurance_department = models.CharField(max_length=10, null=True, blank=True,
                                                                            choices=independant_quality_assurance_department_CHOICES,
                                                                            default='')
    production_planned_systamatically_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    is_production_planned_systamatically = models.CharField(max_length=10, null=True, blank=True,
                                                            choices=production_planned_systamatically_CHOICES,
                                                            default='')

    production_plan_details = models.CharField(max_length=500, null=True, blank=True)
    production_planning_and_control_system_CHOICES = (
        ('Work Procedure', 'Work Procedure'),
        ('Index Cards', 'Index Cards'),

    )
    production_planning_and_control_system = models.CharField(max_length=100, null=True, blank=True,
                                                              choices=production_planning_and_control_system_CHOICES,
                                                              default='')
    is_delivery_timed_planned_and_monitored_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    is_delivery_timed_planned_and_monitored = models.CharField(max_length=10, null=True, blank=True,
                                                               choices=is_delivery_timed_planned_and_monitored_CHOICES,
                                                               default='')
    is_inform_customer_of_delay_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    is_inform_customer_of_delay = models.CharField(max_length=10, null=True, blank=True,
                                                   choices=is_inform_customer_of_delay_CHOICES, default='')
    is_work_instruction_for_production_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    is_work_instruction_for_production = models.CharField(max_length=10, null=True, blank=True,
                                                          choices=is_work_instruction_for_production_CHOICES,
                                                          default='')
    is_work_instruction_for_in_process_inspection_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    is_work_instruction_for_in_process_inspection = models.CharField(max_length=10, null=True, blank=True,
                                                                     choices=is_work_instruction_for_in_process_inspection_CHOICES,
                                                                     default='')
    is_work_instruction_for_final_inspection_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    is_work_instruction_for_final_inspection = models.CharField(max_length=10, null=True, blank=True,
                                                                choices=is_work_instruction_for_final_inspection_CHOICES,
                                                                default='')
    is_work_instruction_for_outgoing_goods_inspection_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    is_work_instruction_for_outgoing_goods_inspection = models.CharField(max_length=10, null=True, blank=True,
                                                                         choices=is_work_instruction_for_outgoing_goods_inspection_CHOICES,
                                                                         default='')
    is_inspection_work_result_documented_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    is_inspection_work_result_documented = models.CharField(max_length=10, null=True, blank=True,
                                                            choices=is_inspection_work_result_documented_CHOICES,
                                                            default='')
    one_time_delivery_compalince_last_or_current_year_percentage = models.CharField(max_length=50, null=True,
                                                                                    blank=True)
    implemented_procedure_for_ensuring_non_conforming_products = models.CharField(max_length=50, null=True, blank=True)
    written_work_instructions_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),

    )
    written_work_instructions_for_the_production_processes = models.CharField(max_length=5, null=True, blank=True,
                                                                              choices=written_work_instructions_CHOICES,
                                                                              default='')
    sendto_buyer_date = models.DateTimeField(null=True, blank=True)
    filled_personname = models.CharField(max_length=50, null=True, blank=True)
    filled_persondesignation = models.CharField(max_length=50, null=True, blank=True)
    filled_personsignature = models.FileField(null=True, blank=True, upload_to='signature_docs')
    
    



class b10_material_inspection_testing_equipment_services_questionnaire_details_header(models.Model):
     material_inspection_questionnaire_details_header_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

     created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
     
     modified_date = models.DateTimeField(null=True, blank=True)
    
     liquid_penetrant_inspection=models.BooleanField(null=True, blank=True)
     liquid_penetrant_inspection_means=models.CharField(max_length=100, null=True, blank=True)
     magnetic_particle_test=models.BooleanField(null=True, blank=True)
     magnetic_particle_test_means=models.CharField(max_length=100, null=True, blank=True)
     magnetic_particle_test_equipment=models.CharField(max_length=100, null=True, blank=True)
     ultrasonic_test=models.BooleanField(null=True, blank=True)
     ultrasonic_test_equipment=models.CharField(max_length=100, null=True, blank=True)
     radio_graphic_test_with_xray_tube=models.BooleanField(null=True, blank=True)
     radio_graphic_test_with_xray_tube_equipment=models.CharField(max_length=100, null=True, blank=True)
     radio_graphic_test_with_gama_radiation=models.BooleanField(null=True, blank=True)
     radio_graphic_test_with_gama_radiation_elements=models.CharField(max_length=100, null=True, blank=True)
     pressure_test=models.BooleanField(null=True, blank=True)
     pressure_test_type=models.CharField(max_length=100, null=True, blank=True)
     leak_test=models.BooleanField(null=True, blank=True)
     leak_test_type=models.CharField(max_length=100, null=True, blank=True)
     identification_test=models.BooleanField(null=True, blank=True)
     identification_test_type=models.CharField(max_length=100, null=True, blank=True)
     diamensional_check_mannual=models.BooleanField(null=True, blank=True)
     diamensional_check_mannual_equipment=models.CharField(max_length=100, null=True, blank=True)
     diamensional_check=models.BooleanField(null=True, blank=True)
     three_d_measuring_machine=models.BooleanField(null=True, blank=True)
     tension_test=models.BooleanField(null=True, blank=True)
     hot_tension_test_temp=models.CharField(max_length=100, null=True, blank=True)
     notched_bar_impact_bending_test=models.BooleanField(null=True, blank=True)
     notched_bar_impact_bending_test_temp_from=models.CharField(max_length=100, null=True, blank=True)
     notched_bar_impact_bending_test_temp_to=models.CharField(max_length=100, null=True, blank=True)
     iso_v_specimen=models.BooleanField(null=True, blank=True)
     charpy_v_notch_specimen=models.BooleanField(null=True, blank=True)
     hardness_test=models.BooleanField(null=True, blank=True)
     brinell=models.BooleanField(null=True, blank=True)
     vickers=models.BooleanField(null=True, blank=True)
     rockwell=models.BooleanField(null=True, blank=True)
     other_mechanical_test=models.BooleanField(null=True, blank=True)
     other_mechanical_test_detail=models.CharField(max_length=100, null=True, blank=True)
     macro=models.BooleanField(null=True, blank=True)
     micro=models.BooleanField(null=True, blank=True)
     intergrannular_corrosion=models.BooleanField(null=True, blank=True)
     wet_analysis=models.BooleanField(null=True, blank=True)
     spectro_scopic_analysis=models.BooleanField(null=True, blank=True)
     sand_analysis_for_foundry_sand=models.BooleanField(null=True, blank=True)
     other_chemical_analysis_method=models.BooleanField(null=True, blank=True)
     other_chemical_analysis_method_detail=models.CharField(max_length=100, null=True, blank=True)
     is_regular_checking_of_measuring_equipment=models.BooleanField(null=True, blank=True)  
     is_records_traceable=models.BooleanField(null=True, blank=True)
     is_samples_marked_with_heat_no=models.BooleanField(null=True, blank=True)
     is_records_traceable_to_heat_no=models.BooleanField(null=True, blank=True)
     is_part_marked_with_heat_no=models.BooleanField(null=True, blank=True)
     is_heat_no_traceable_to_furnace_change=models.BooleanField(null=True, blank=True)
     is_prototype_parts_checked_internally=models.BooleanField(null=True, blank=True)
     prototype_parts_checking_method=models.CharField(max_length=100, null=True, blank=True)
     is_parts_checked_by_random_sampling=models.BooleanField(null=True, blank=True)
     random_sampling_checking_method=models.CharField(max_length=100, null=True, blank=True)
     is_welding_procedure_qualified=models.BooleanField(null=True, blank=True)
     welding_procedure_qualified_standard=models.CharField(max_length=100, null=True, blank=True)
     is_welders_qualified=models.BooleanField(null=True, blank=True)
     welders_qualified_standard=models.CharField(max_length=100, null=True, blank=True)
     is_defects_checked_prior_to_welding=models.BooleanField(null=True, blank=True)
     certiticate_file=models.FileField(null=True, blank=True, upload_to='certiticate_file')
     defective_material_identification_method=models.CharField(max_length=100, null=True, blank=True)
     reject_rework_rate=models.CharField(max_length=100, null=True, blank=True)
     foundary_forge_shop_intern_reject_rework_rate=models.CharField(max_length=100, null=True, blank=True)
     foundary_forge_shop_extern_reject_rework_rate=models.CharField(max_length=100, null=True, blank=True)
     machining_reject_rework_rate=models.CharField(max_length=100, null=True, blank=True)
     finished_product_reject_rework_rate=models.CharField(max_length=100, null=True, blank=True)
     sendto_buyer_date = models.DateTimeField(null=True, blank=True)
     filled_personname=models.CharField(max_length=50, null=True, blank=True)
     filled_persondesignation=models.CharField(max_length=50, null=True, blank=True)
     filled_personsignature=models.FileField(null=True, blank=True, upload_to='signature_docs')