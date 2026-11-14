from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from json import loads
from crm.models import Employee

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class EmployeeListCreateView(View):
    def get(self,request):
        
        qs = Employee.objects.all().values() #=> data type = query set
        
        response_data = list(qs) # qs => PYNT
        
        return JsonResponse(response_data,safe=False) # PYNT =>JSON
    
    def post(self,request):
        
        json_data = request.body
        
        form_data = loads(json_data)
        
        """
        {
            "name":"hari",
            "email":"hari@gmail.com",
            "phone":"234567890",
            "salary":55000,
            "department":"hr",
            "location":"kakkanad"
        }
        """
        
        Employee.objects.create(
            name=form_data.get("name"),
            email=form_data.get("email"),
            phone=form_data.get("phone"),
            salary=form_data.get("salary"),
            department=form_data.get("department"),
            location=form_data.get("location")
        )
        
        response_data = {"message":"emplyee created"}
        
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")       
class EmployeeRetrieveUpdateView(View):
    def get(self,request,pk=None):
        qs = Employee.objects.filter(id=pk).values()
        
        response_data = list(qs)
        
        return JsonResponse(response_data,safe=False)
    
    def put(self,request,pk=None):
        
        json_data = request.body
        form_data = loads(json_data)
        Employee.objects.filter(id=pk).update(**form_data)
        responnse_data = {"message":"employee updated"}
        
        return JsonResponse(responnse_data)
    
    def delete(self,request,pk=None):
        Employee.objects.filter(id=pk).delete()
        
        response_data = {"message":"employee deleted"}
        
        return JsonResponse(response_data)
    