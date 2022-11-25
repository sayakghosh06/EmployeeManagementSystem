from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Role,Department
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()

    context={
        'emps': emps
    }
   
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        role=request.POST['role']
        phone=request.POST['phone']
        hire_date=request.POST['hire_date']
        new_emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept,salary=salary,bonus=bonus,role_id=role,phone=phone,hire_date=hire_date)
        new_emp.save()
        messages.success(request,"Employee Added Successfully")
        
    
    return render(request,'add_emp.html')

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            messages.success(request,"Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)



def filter_emp(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')


