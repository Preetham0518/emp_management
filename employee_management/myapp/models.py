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


