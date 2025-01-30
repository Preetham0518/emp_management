from django.db import connection


def get_department():
    query  = "SELECT department_id,name,description FROM myapp_department"
    with connection.cursor() as cursor:
        cursor.execute(query)
        department = cursor.fetchall()
    return [{'department_id':d[0],'name':d[1],'description':d[2]} for d in department]


def get_designation():
    query = """SELECT d.designation_id, d.designation_name,d.designation_description,
    dep.department_id,
    dep.name AS department_name
     
    FROM myapp_designation d
     
    JOIN myapp_department dep
    
    ON d.department_id_id = dep.department_id
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        designation = cursor.fetchall()

    return [{'designation_id':d[0],'designation_name':d[1],'designation_description':d[2],
            'department_id':d[3],'department_name':d[4]} for d in designation]
    
    
def get_location():
    query = "SELECT location_id,name,description FROM myapp_location"
    with connection.cursor() as cursor:
        cursor.execute(query)
        location = cursor.fetchall()
    return[{'location_id':l[0],'name':l[1],'description':l[2]} for l in location]

def get_employees():
    query = """SELECT e.employee_id, e.name,e.contact,e.emp_start_date,e.emp_end_date,e.employee_no,e.join_date,e.address,e.status,dep.name AS department_name,d.designation_name,
    l.name AS location_name
    FROM myapp_employee e
    JOIN myapp_department dep ON e.department_id = dep.department_id
    JOIN myapp_designation d ON e.designation_id = d.designation_id
    JOIN myapp_location l ON e.location_id = l.location_id
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        employee = cursor.fetchall()
    return[{'employee_id':e[0],'name':e[1],'contact':e[2],'emp_start_date':e[3],'emp_end_date':e[4],'employee_no':e[5],'join_date':e[6],'address':e[7],'status':e[8],'department_name':e[9],'designation_name':e[10],
            'location_name':e[11]} for e in employee]
    