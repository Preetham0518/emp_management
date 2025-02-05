"""
URL configuration for employee_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request:redirect('user_login/')),
    path('departments/', department_list, name="department_list"),
    path('department_add/',department_add,name="department_add" ),
    path('department_update/<str:pk>/', department_update, name="department_update"),
    path('department_view/<str:pk>/', department_view, name="department_view"),
    path('designation/', designation_list, name="designation_list"),
    path('designation_add/', designation_add, name="designation_add"),
    path('designation_update/<str:pk>/', designation_update, name="designation_update"),
    path('designation_view/<str:pk>/', designation_view, name="designation_view"),
    path('location/',location_list,name="location_list"),
    path('location_add/',location_add,name="location_add"),
    path('location_update/<str:pk>/', location_update,name="location_update"),
    path('location_view/<str:pk>/',location_view,name="location_view"),
    path('employee/', employee_list,name="employee_list"),
    path('employee_add',employee_add,name="employee_add"),
    path('employee_update/<str:employee_id>/',employee_update,name="employee_update"),
    path('employee_view/<str:pk>/',employee_view,name="employee_view"),
    path('register/',register,name="register"),
    path('user_login/',user_login,name="user_login"),
    path('logoutUser/',logoutUser,name="logoutUser"),
    path('user_list/',user_list,name="user_list"),
    path('userlist_add/',userlist_add,name="userlist_add"),
    path('userlist_update/<int:pk>/',userlist_update,name="userlist_update"),
    path('user_delete/<str:pk>/',user_delete,name="user_delete"),
    path('reportlist/',reportlist,name="reportlist"),
    path('Download/',Download,name="Download"),
    path('employee_pdf/<str:employee_id>/',employee_pdf,name="employee_pdf"),
    path('send_email/<str:employee_id>/',send_email,name="send_email"),
    path('department_export', department_export, name="department_export"),
    path('designation_export', designation_export, name="designation_export"),
    path('department_upload',department_upload,name="department_upload"),
    path('designation_upload',designation_upload,name="designation_upload"),
    path('employee_upload',employee_upload,name="employee_upload"),
    path('department_delete/<str:pk>/', department_delete,name="department_delete"),
    path('designation_delete/<str:pk>/', designation_delete,name="designation_delete"),
    path('location_delete/<str:pk>/', location_delete, name="location_delete"),
    path('employee_export',employee_export,name="employee_export"),
    path('ajax/load-designations/', load_designations, name='load_designations'),
    path('department_data/',department_data,name="department_data"),
    path('designation_data/',designation_data,name="designation_data"),
    path('location_data/',location_data,name="location_data"),
    path('employee_data/',employee_data,name="employee_data"),
    path('report_data/',report_data,name="report_data"),
    path('employee_delete/<str:pk>/',employee_delete,name="employee_delete"),
    path('generalOrganization/',generalOrganization_list,name="generalOrganization_list"),
    path('generalOrganization_add/',generalOrganization_add,name="generalOrganization_add"),
    path('generalOrganization_update/<uuid:pk>/',generalOrganization_update,name="generalOrganization_update"),
    path('generalOrganization_pdf/<uuid:pk>/',generalOrganization_pdf,name="generalOrganization_pdf"),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    
