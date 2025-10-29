from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def retrieve_view(request):
    emp_list=Employee.objects.all()
   # emp_list=Employee.objects.filter(esal__range=[12000,15000])
    return render(request,'testapp/index.html',{'emp_list':emp_list})