import pandas as pd
from django.shortcuts import render, redirect
from .models import Department, Designation , Location , Employee, Skill
from .forms import DepartmentForm, DesignationForm , LocationForm, EmployeeForm,SkillForm,CreateUserForm, UploadFileForm
from django.shortcuts import get_object_or_404
from .forms import SkillFormSet
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.http import HttpResponse
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from django.core.mail import send_mail
from django.conf import settings 
from django.core.mail.message import EmailMessage
from io import BytesIO
from django.http import JsonResponse
from .database_query import get_department, get_designation, get_location, get_employees
from datetime import datetime
from django.utils.dateparse import parse_date
from django.core.paginator import Paginator
from django.db import transaction

# Create your views here.
@unauthenticated_user
def register(request):
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                default_group_name = 'users' 
                default_group, created = Group.objects.get_or_create(name=default_group_name)
                user.groups.add(default_group)
                
                
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {username}')
                return redirect('user_login')
            else:
                print(form.errors)
                messages.error(request, 'Invalid Information')
            
        else:
            form = CreateUserForm()
        return render(request, 'accounts/register.html', {'form': form})

    
    
@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('department_list')
        else:
            messages.error(request, 'Username or Password is incorrect')
    return render(request,'accounts/login.html')
    

def logoutUser(request):
    logout(request)
    return redirect('user_login')


@login_required(login_url='user_login')
def department_list(request):
    departments = get_department()
    logged_in_user = request.user
    is_admin = logged_in_user.groups.filter(name='admin').exists()
    return render(request, 'master/department_list.html', {'departments': departments,'logged_in_user':logged_in_user,'is_admin': is_admin})

@login_required(login_url='user_login')
def department_add(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.created_by = request.user
            department.updated_by = request.user
            form.save()
            messages.success(request, "Department added Successfully")
            return redirect('department_list')
        else:
            return render(request, 'master/department_add.html', {'form': form})
    else:
        form = DepartmentForm()
    
    return render(request, 'master/department_add.html', {'form': form})

@login_required(login_url='user_login')
def department_update(request,pk):
    obj = get_object_or_404(Department, pk=pk)
    
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=obj)
        if form.is_valid():
            department = form.save(commit=False)
            department.created_by = request.user
            department.updated_by = request.user
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=obj)
    return render(request,'master/department_edit.html',{'form':form})

@login_required(login_url='user_login')
def department_view(request,pk):
    obj = get_object_or_404(Department,pk=pk)
    return render(request, 'master/department_view.html', {'obj':obj})

@login_required(login_url='user_login')
def designation_list(request):
    designations = get_designation()
    logged_in_user = request.user
    is_admin = logged_in_user.groups.filter(name='admin').exists()
    return render(request, 'master/designationlist.html',{'designations':designations,'logged_in_user':logged_in_user,'is_admin':is_admin})

@login_required(login_url='user_login')
def designation_add(request):
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            designation = form.save(commit=False)
            designation.created_by = request.user
            designation.updated_by = request.user
            form.save()
            return redirect('designation_list')  
    else:
        form = DesignationForm() 
    return render(request, 'master/designation_add.html', {'form': form})

@login_required(login_url='user_login')
def designation_update(request,pk):
    designation = get_object_or_404(Designation, pk=pk)
    if request.method == 'POST':
        form=DesignationForm(request.POST, instance=designation)
        if form.is_valid():
            designation = form.save(commit=False)
            designation.created_by = request.user
            designation.updated_by = request.user
            form.save()
            return redirect('designation_list')
        
    else:
        form = DesignationForm(instance=designation)
    return render(request, 'master/designation_edit.html',{'form':form})

@login_required(login_url='user_login')
def designation_view(request,pk):
    designation = get_object_or_404(Designation,pk=pk)
    return render(request, 'master/designation_view.html',{'designation':designation})

@login_required(login_url='user_login')
def location_list(request):
    locations = get_location()
    logged_in_user = request.user
    is_admin = logged_in_user.groups.filter(name='admin').exists()
    return render(request,'master/locationlist.html',{'locations':locations,'logged_in_user':logged_in_user,'is_admin':is_admin})

@login_required(login_url='user_login')
def location_add(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.created_by = request.user
            location.updated_by = request.user
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm()
    return render(request,'master/location_add.html',{'form':form})


@login_required(login_url='user_login')
def location_update(request,pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('location_list')
    else:
        form = LocationForm(instance=location)
    return render(request,'master/location_edit.html',{'form':form})

@login_required(login_url='user_login')
def location_view(request,pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request,'master/location_view.html',{'location':location})


@login_required(login_url='user_login')
def employee_list(request):
    employees = get_employees()
    logged_in_user = request.user
    is_admin = logged_in_user.groups.filter(name='admin').exists()
    return render(request,'employee/employeelist.html',{'employees':employees,'logged_in_user':logged_in_user,'is_admin':is_admin})


@login_required(login_url='user_login')
def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        formset = SkillFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            employee = form.save(commit=False)  
            employee.created_by = request.user  
            employee.updated_by = request.user
            employee = form.save()
            for skill_form in formset:
                skill = skill_form.save(commit=False)
                skill.employee = employee
                skill.save()
            return redirect('employee_list')
        
    else:
        form = EmployeeForm()
        formset = SkillFormSet(queryset=Skill.objects.none())
    return render(request,'employee/employee_add.html',{'form':form,'formset':formset})


# def employee_update(request, employee_id):
#     employee = get_object_or_404(Employee, employee_id=employee_id)
#     SkillFormSet = modelformset_factory(Skill,form=SkillForm,extra=0)

#     if request.method == 'POST':
#         form = EmployeeForm(request.POST, request.FILES, instance=employee)
#         formset = SkillFormSet(request.POST,queryset=Skill.objects.filter(employee=employee))
        
#         if form.is_valid() and formset.is_valid():
#             employee = form.save(commit=False)  
#             employee.created_by = request.user  
#             employee.updated_by = request.user
#             employee = form.save()
#             for skill_form in formset:
#                 if skill_form.cleaned_data.get('DELETE',False):
#                     skill_form.instance.delete()
#                 else:
#                     skill = skill_form.save(commit=False)
#                     skill.employee = employee
#                     skill.save()
#             return redirect('employee_list')
#         else:
#             if not form.is_valid():
#                 print("Form Errors:",form.errors)
#             if not formset.is_valid():
#                 print("Individual Form Errors:",formset.errors)
#     else:
#         form = EmployeeForm(instance=employee)
#         formset = SkillFormSet(queryset=Skill.objects.filter(employee=employee))
#     return render(request, 'employee/employee_edit.html', 
#                   {'form': form,
#                     'formset':formset,
#                     'current_department':employee.department_id,
#                     'current_designation':employee.designation_id,})
@login_required(login_url='user_login')
def employee_update(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    
    # Configure SkillFormSet with your custom SkillForm
    SkillFormSet = modelformset_factory(
        Skill,
        form=SkillForm,
        extra=1,
        can_delete=True,
        fields=('skill_name', 'description')
    )
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        formset = SkillFormSet(
            request.POST,
            queryset=Skill.objects.filter(employee=employee),
            prefix='form'
        )
        
        try:
            with transaction.atomic():
                if form.is_valid() and formset.is_valid():
                    # Save employee
                    employee = form.save(commit=False)
                    employee.updated_by = request.user
                    employee.save()
                    
                    # Process skills
                    for skill_form in formset:
                        if skill_form.cleaned_data:
                            if skill_form.cleaned_data.get('DELETE', False):
                                if skill_form.instance.pk:
                                    skill_form.instance.delete()
                            else:
                                skill = skill_form.save(commit=False)
                                skill.employee = employee
                                skill.save()
                    
                    messages.success(request, 'Employee details updated successfully!')
                    return redirect('employee_list')
                else:
                    if form.errors:
                        messages.error(request, 'Please correct the errors in the employee form.')
                    if formset.errors:
                        messages.error(request, 'Please correct the errors in the skills form.')
                    print("Form errors:", form.errors)
                    print("Formset errors:", formset.errors)
        
        except Exception as e:
            messages.error(request, f'An error occurred while updating: {str(e)}')
            print("Exception:", str(e))
    
    else:
        form = EmployeeForm(instance=employee)
        formset = SkillFormSet(
            queryset=Skill.objects.filter(employee=employee),
            prefix='form'
        )
    
    context = {
        'form': form,
        'formset': formset,
        'current_department': employee.department_id,
        'current_designation': employee.designation_id,
        'employee': employee
    }
    
    return render(request, 'employee/employee_edit.html', context)                                                        
                                                           


@login_required(login_url='user_login')
def employee_view(request,pk):
    employee = get_object_or_404(Employee, pk=pk)
    skills = employee.skills.all()
    return render(request,'employee/employee_view.html',{'employee':employee,'skills':skills})

def employee_delete(request,pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, "Employee deleted Successfully")
    return redirect('employee_list')


@login_required(login_url='user_login')
def user_list(request):
    users = User.objects.all()
    logged_in_user = request.user
    is_admin = logged_in_user.groups.filter(name='admin').exists()
    return render(request,'accounts/user_list.html',{'users':users,'logged_in_user':logged_in_user,'is_admin':is_admin})


@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def userlist_add(request):
    if not request.user.groups.filter(name='admin').exists():
        return redirect('user_list')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_name = form.cleaned_data.get('user_type')
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            return redirect('user_list')
    else:
        form = CreateUserForm()
            
    return render(request,'accounts/userlist_add.html',{'form':form})
  
@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])    
def userlist_update(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance = user)
        if form.is_valid():
            user = form.save()
            group_name = form.cleaned_data.get('user_type')
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.clear()
            user.groups.add(group)
            return redirect('user_list')
    else:
        form = CreateUserForm(instance=user)
    return render(request,'accounts/userlist_edit.html',{'form':form})



@login_required(login_url='user_login')
def Download(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    report = get_employees()
    
    if start_date:
        filter_start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        report = [emp for emp in report if emp['emp_start_date'] and emp['emp_start_date'] >= filter_start_date]

    # Apply end_date filter if provided, or include employees with no end_date
    if end_date:
        filter_end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        report = [emp for emp in report if emp['emp_end_date'] and emp['emp_end_date'] <= filter_end_date]
    else:
        report = [emp for emp in report if emp['emp_end_date'] is None]
    
        report_values = [
        {
            'employee_id': emp.get('employee_id'),
            'name': emp.get('name'),
            'contact': emp.get('contact'),
            'emp_start_date': emp.get('emp_start_date'),
            'emp_end_date': emp.get('emp_end_date'),
            'employee_no': emp.get('employee_no'),
            'join_date': emp.get('join_date'),
            'address': emp.get('address'),
            'status': emp.get('status'),
            'department_name': emp.get('department_name'), 
            'designation_name': emp.get('designation_name'),  
            'location_name': emp.get('location_name')  
        }
        for emp in report
    ]
    df = pd.DataFrame(list(report_values))
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Employeelist_Report.xlsx'
    
    df.to_excel(response,index=False, engine='openpyxl')
    return response


@login_required(login_url='user_login')
def reportlist(request):
    start_date = (request.GET.get('start_date'))
    end_date = (request.GET.get('end_date'))
    report = get_employees()

    if start_date:
        report = [emp for emp in report if emp.get('start_date') and emp['start_date'] >= start_date]
    
    if end_date:
        report = [emp for emp in report if emp.get('end_date') and emp['end_date'] <= end_date]
    else:
        report = [emp for emp in report if emp.get('end_date') is None]

    return render(request, 'reports/reportlist.html', {'report': report})



@login_required(login_url='user_login')
def employee_pdf(request,employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition']=f'attachment;filename="{employee.name}.pdf"'
    
    p = canvas.Canvas(response, pagesize=letter)
    
    y_position = 750

    if employee.photo:
        p.drawImage(employee.photo.path, 100, y_position - 150, width=150, height=150)
        y_position -= 170
        
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, y_position, "Employee Details")
    y_position -= 30 
     
    
    p.setFont("Helvetica", 12)
    p.drawString(100, y_position, f"Employee ID:{employee.pk}")
    y_position -= 20
    p.drawString(100, y_position, f"Name:{employee.name}")
    y_position -= 20
    p.drawString(100, y_position, f"Contact:{employee.contact}")
    y_position -= 20
    p.drawString(100, y_position, f"Employee No:{employee.employee_no}")
    y_position -= 20
    p.drawString(100, y_position, f"Address:{employee.address}")
    y_position -= 20
    p.drawString(100, y_position, f"Department:{employee.department.name}")
    y_position -= 20
    p.drawString(100, y_position, f"Designation:{employee.designation.designation_name}")
    y_position -= 20
    p.drawString(100, y_position, f"Location:{employee.location.name}")
    y_position -= 20
    
    p.showPage()
    p.save()
    return response



@login_required(login_url='user_login')    
def send_email(request, employee_id):
    if request.method == "POST":
        recipient_email = request.POST.get("recipient_email")
        if not recipient_email:
            return JsonResponse({"error": "Recipient email is required."}, status=400)

        try:
            employee = get_object_or_404(Employee, employee_id=employee_id)

            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            y_position = 820
            if employee.photo:
                p.drawImage(employee.photo.path, 100, y_position - 150, width=150, height=150)
                y_position -= 170
            
            p.drawString(100, y_position, f"Employee ID: {employee.employee_id}")
            y_position -= 20
            p.drawString(100,y_position, f"Employee Details: {employee.name}")
            y_position -= 20
            p.drawString(100, y_position,f"Employee No: {employee.employee_no}")
            y_position -= 20
            p.drawString(100, y_position, f"Contact: {employee.contact}")
            y_position -= 20
            p.drawString(100, y_position, f"Address: {employee.address}")
            y_position -= 20
            p.drawString(100, y_position, f"Department: {employee.department.name}")
            y_position -= 20
            p.drawString(100, y_position, f"Designation: {employee.designation.designation_name}")
            y_position -= 20
            p.drawString(100, y_position, f"Location: {employee.location.name}")
            y_position -=20
            p.showPage()
            p.save()
            buffer.seek(0)

            subject = f"Employee Details: {employee.name}"
            body = f"Please find attached details of {employee.name}."
            from_email = "sai.preetham0518@gmail.com" 
            email = EmailMessage(subject, body, from_email, [recipient_email])
            email.attach(f"{employee.name}_details.pdf", buffer.getvalue(), "application/pdf")

            
            email.send()
            messages.success(request, "Email sent successfully.")
            
        except Exception as e:
            (messages.error(request, f"An error occurred: {e}"))
            
    return redirect('employee_list')

@login_required(login_url='user_login')  
def department_export(request):
    export = Department.objects.all()
   
    
    export_values = export.values(
        'department_id','name','description'
    )
    df = pd.DataFrame(list(export_values))
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Department_Report.xlsx'
    
    df.to_excel(response,index=False, engine='openpyxl')
    return response


@login_required(login_url='user_login')         
def designation_export(request):
    export = Designation.objects.all()
   
    
    export_values = export.values(
        'designation_id','designation_name','designation_description',
    )
    df = pd.DataFrame(list(export_values))
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Designation_Report.xlsx'
    
    df.to_excel(response,index=False, engine='openpyxl')
    return response

def employee_export(request):
    export = Employee.objects.all()
   
    
    export_values = export.values(
        'name','contact','department__name','designation__designation_name','location__name'
        
    )
    df = pd.DataFrame(list(export_values))
    
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Employee_Report.xlsx'
    
    df.to_excel(response,index=False, engine='openpyxl')
    return response


@login_required(login_url='user_login')
def department_upload(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            messages.error(request, "Please upload a file.")
            return redirect('department_list')

        file = request.FILES['file']

        if not file.name.endswith(('.xls', '.xlsx')):
            messages.error(request, "Only Excel files (.xls, .xlsx) are allowed.")
            return redirect('department_list')

        try:
            df = pd.read_excel(file)

            if not {'department_id', 'name', 'description'}.issubset(df.columns):
                messages.error(request, "The file must have 'department_id', 'name', and 'description' columns.")
                return redirect('department_list')

            for _, row in df.iterrows():
                Department.objects.create(
                    department_id=row['department_id'],
                    name=row['name'],
                    description=row['description']
                )

            messages.success(request, "File uploaded and data saved successfully!")
        except Exception as e:
            messages.error(request, "There was an error processing the file. Please check the file and try again.")

        return redirect('department_list')

    return redirect('department_list')
    

    
    
@login_required(login_url='user_login')          
def designation_upload(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            messages.error(request, "Please upload a file.")
            return redirect('designation_list')

        file = request.FILES['file']

        if not file.name.endswith(('.xls', '.xlsx')):
            messages.error(request, "Only Excel files (.xls, .xlsx) are allowed.")
            return redirect('designation_list')

        try:
            df = pd.read_excel(file)

            if not {'designation_id', 'designation_name', 'designation_description'}.issubset(df.columns):
                messages.error(request, "The file must have 'designation_id', 'designation_name', and 'designation_description' columns.")
                return redirect('designation_list')

            for _, row in df.iterrows():
                Department.objects.create(
                    department_id=row['designation_id'],
                    name=row['designation_name'],
                    description=row['designation_description']
                )

            messages.success(request, "File uploaded and data saved successfully!")
        except Exception as e:
            messages.error(request, "There was an error processing the file. Please check the file and try again.")

        return redirect('designation_list')

    return redirect('designation_list')


        
@login_required(login_url='user_login')
def employee_upload(request):
    if request.method == 'POST':
       
        if 'file' not in request.FILES:
            messages.error(request, "Please upload a file.")
            return redirect('employee_list')

        file = request.FILES['file']

        
        if not file.name.endswith(('.xls', '.xlsx')):
            messages.error(request, "Only Excel files (.xls, .xlsx) are allowed.")
            return redirect('employee_list')

        try:
            
            df = pd.read_excel(file, dtype={'join_date': str, 'emp_start_date': str, 'emp_end_date': str})

            
            required_columns = [
                'employee_id', 'join_date', 'employee_no', 'name', 'contact', 'address',
                'emp_start_date', 'emp_end_date', 'status', 'department__name',
                'designation__designation_name', 'location__name'
            ]
            if not set(required_columns).issubset(df.columns):
                messages.error(request, "The file must contain these columns: " + ", ".join(required_columns))
                return redirect('employee_list')

           
            for index, row in df.iterrows():
                
                department = Department.objects.filter(name=row['department__name']).first()
                designation = Designation.objects.filter(designation_name=row['designation__designation_name']).first()
                location = Location.objects.filter(name=row['location__name']).first()

                if not (department and designation and location):
                    messages.error(request, f"Missing ForeignKey data in row {index + 1}. Skipping this row.")
                    continue

                
                try:
                    join_date = datetime.strptime(row['join_date'], '%Y-%m-%d').date()
                    emp_start_date = datetime.strptime(row['emp_start_date'], '%Y-%m-%d').date()
                    emp_end_date = None
                    if pd.notna(row['emp_end_date']):
                        emp_end_date = datetime.strptime(row['emp_end_date'], '%Y-%m-%d').date()
                except ValueError:
                    messages.error(request, f"Invalid date format in row {index + 1}. Skipping this row.")
                    continue

                
                Employee.objects.create(
                    employee_id=row['employee_id'],
                    join_date=join_date,
                    employee_no=row['employee_no'],
                    name=row['name'],
                    contact=row['contact'],
                    address=row['address'],
                    emp_start_date=emp_start_date,
                    emp_end_date=emp_end_date,
                    status=row['status'],
                    department=department,
                    designation=designation,
                    location=location
                )

            messages.success(request, "Employee data uploaded successfully.")
        except Exception as e:
            messages.error(request, f"An error occurred while processing the file: {e}")
        
        return redirect('employee_list')

    return redirect('employee_list')




    
@login_required(login_url='user_login')  
def department_delete(request,pk):
    department = get_object_or_404(Department, pk=pk)
    if Employee.objects.filter(department=department).exists():
        messages.error(request, "Department is used and cannot be deleted")
        return redirect('department_list')
        
    if request.method == 'POST':
        department.delete()
        messages.success(request, "Department deleted Successfully")
        return redirect('department_list')
    
@login_required(login_url='user_login')     
def designation_delete(request,pk):
    designation = get_object_or_404(Designation, pk=pk)
    if Employee.objects.filter(designation=designation).exists():
        messages.error(request, "Designation is used and cannot be deleted")
        return redirect('designation_list')
        
    if request.method == 'POST':
        designation.delete()
        messages.success(request, "Designation deleted Successfully")
        return redirect('designation_list')
    
@login_required(login_url='user_login')
def location_delete(request,pk):
    location = get_object_or_404(Location, pk=pk)
    if Employee.objects.filter(location=location).exists():
        messages.success(request, "location is used and cannot be deleted")
        return redirect('location_list')
        
    if request.method == 'POST':
        location.delete()
        messages.success(request, "Location deleted Successfully")
        return redirect('location_list')
    



@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def user_delete(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.success(request,"User deleted Successfully")
    return redirect('user_list')


def load_designations(request):
    department_id = request.GET.get('department_id')
    designations = Designation.objects.filter(department_id=department_id)
    data =list(designations.values('designation_id','designation_name'))
    return JsonResponse(data, safe=False)


def department_data(request):
    start_index = int(request.GET.get('start', 0))
    page_length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '').strip()
    draw = int(request.GET.get('draw', 1))

    departments = get_department()  # This should return a QuerySet or List

    total_records = len(departments)


    if search_value:
        departments = [dept for dept in departments if search_value.lower() in dept['name'].lower()]

    filtered_records = len(departments)

    # Apply pagination
    departments = departments[start_index:start_index + page_length]

    # Format response data
    data = [
        {
            'department_id': department['department_id'],
            'name': department['name'],
            'description': department['description'],
        }
        for department in departments
    ]

    response = {
        'draw': draw,  
        'recordsTotal': total_records,  
        'recordsFiltered': filtered_records,  
        'data': data,  
    }

    return JsonResponse(response)

def designation_data(request):
    start_index = int(request.GET.get('start', 0))
    page_length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '').strip()
    draw = int(request.GET.get('draw', 1))
    
    designations = get_designation()
    
    if search_value:
        designations = [d for d in designations if search_value.lower() in d['designation_name'].lower()]

       
    total_records = len(designations)

       
    designations = designations[start_index:start_index + page_length]
        
    filtered_records = len(designations)

        
    data = [
            {
                'designation_id': designation['designation_id'],
                'designation_name': designation['designation_name'],
                'designation_description': designation['designation_description'],
            }
            for designation in designations
        ]

        #
    response = {
            'draw': draw,   
            'recordsTotal': total_records,
            'recordsFiltered': filtered_records,  
            'data': data, 
        }

    return JsonResponse(response)




def location_data(request):
    start_index = int(request.GET.get('start', 0))
    page_length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '').strip()
    draw = int(request.GET.get('draw', 1))
    locations = get_location()
    if search_value:
        locations = [loc for loc in locations if search_value.lower() in loc['name'].lower()]

        
    total_records = len(locations)

       
    filtered_records = len(locations)

       
    locations = locations[start_index:start_index + page_length]

        
    data = [
            {
                'location_id': locations['location_id'],
                'name': locations['name'],
                'description': locations['description'],
            }
            for locations in locations
        ]

        #
    response = {
            'draw': draw,  
            'recordsTotal': total_records,  
            'recordsFiltered': filtered_records,  
            'data': data, 
        }

    return JsonResponse(response)

def employee_data(request):
    start_index = int(request.GET.get('start', 0))
    page_length = int(request.GET.get('length', 10))
    search_value = request.GET.get('search[value]', '').strip()
    draw = int(request.GET.get('draw', 1))

        
    employees = get_employees()
    if search_value:
        employees = [emp for emp in employees if search_value.lower() in emp['name'].lower()]

        
    total_records = len(employees)

       
    filtered_records = len(employees)
       
    employees = employees[start_index:start_index + page_length]

        
    data = [
        {
            'employee_id': employee['employee_id'],  
            'name': employee['name'],
            'contact': employee['contact'],
            'department': employee.get('department_name', 'No Department'),
            'designation': employee.get('designation_name','No Designation'),
            'location': employee.get('location_name','No Location'),
        }
            for employee in employees
        ]

        #
    response = {
            'draw': draw,  
            'recordsTotal': total_records,  
            'recordsFiltered': filtered_records,  
            'data': data, 
        }

    return JsonResponse(response)



# def report_data(request):
#     start_index = int(request.GET.get('start', 0))  
#     page_length = int(request.GET.get('length', 10))  
#     search_value = request.GET.get('search[value]', '').strip()  
#     draw = int(request.GET.get('draw', 1))
   
#     report = get_employees()
    
    
#     if search_value:
#         report = [emp for emp in report if search_value.lower() in emp["name"].lower()]


#     total_records = len(report)
#     filtered_records = len(report)
#     report = report[start_index:start_index + page_length]
    
#     data = [
#         {
#             'name': emp['name'],
#             'contact': emp['contact'],
#             'department_name': emp.get('department_name'),
#             'designation_name': emp.get('designation_name'),
#             'status': emp.get("status", "active"),
#         }
#         for emp in report
#     ]

#     response = {
#         'draw': draw,  
#         'recordsTotal': total_records,  
#         'recordsFiltered': filtered_records, 
#         'data': data,  
#     }

#     return JsonResponse(response)



def report_data(request):
    start_index = int(request.GET.get('start', 0))  
    page_length = int(request.GET.get('length', 10))  
    search_value = request.GET.get('search[value]', '').strip()  
    draw = int(request.GET.get('draw', 1)) 

    
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

   
    report = get_employees()

    for emp in report:
        # If emp_start_date is a string, convert it to a date
        if emp['emp_start_date'] and isinstance(emp['emp_start_date'], str):
            emp['emp_start_date'] = datetime.strptime(emp['emp_start_date'], '%Y-%m-%d').date()

        # If emp_end_date is a string, convert it to a date
        if emp['emp_end_date'] and isinstance(emp['emp_end_date'], str):
            emp['emp_end_date'] = datetime.strptime(emp['emp_end_date'], '%Y-%m-%d').date()

    # Apply start_date filter if provided
    if start_date:
        filter_start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        report = [emp for emp in report if emp['emp_start_date'] and emp['emp_start_date'] >= filter_start_date]

    # Apply end_date filter if provided, or include employees with no end_date
    if end_date:
        filter_end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        report = [emp for emp in report if emp['emp_end_date'] and emp['emp_end_date'] <= filter_end_date]
    else:
        report = [emp for emp in report if emp['emp_end_date'] is None]


    if search_value:
        report = [emp for emp in report if search_value.lower() in emp["name"].lower()]

    total_records = len(report)

    report = report[start_index:start_index + page_length]
    data = [
        {
            'name': emp['name'],
            'contact': emp['contact'],
            'department_name': emp.get('department_name'),
            'designation_name': emp.get('designation_name'),
            'status': emp.get("status", "active"),
            'emp_start_date': emp['emp_start_date'].strftime('%Y-%m-%d') if emp['emp_start_date'] else None,
            'emp_end_date': emp['emp_end_date'].strftime('%Y-%m-%d') if emp['emp_end_date'] else None
        }
        for emp in report
    ]

    response = {
        'draw': draw,
        'recordsTotal': total_records,  
        'recordsFiltered': len(report),  
        'data': data,  
    }

    return JsonResponse(response)








