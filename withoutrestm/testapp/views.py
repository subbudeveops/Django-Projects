from django.shortcuts import render
from .models import Employee
from django.views.generic import View
from django.http import HttpResponse
import json
# Create your views here.
# Retraive the data from the database and

from django.core.serializers import serialize


class EmployeeDetailView(View):
    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id=id)

        json_data = serialize(
            'json', [emp, ], fields=('eno', 'ename', 'esal'))
        return HttpResponse(json_data, content_type='application/json')
