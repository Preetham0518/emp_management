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
    
    