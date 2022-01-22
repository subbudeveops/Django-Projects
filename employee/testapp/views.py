from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
def Employee_view(request):
  emp=Employee.objects.all()
  return render(request,'testapp/employee.html',{'emp':emp})