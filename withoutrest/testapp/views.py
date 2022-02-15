from django.views.generic import View
from django.http import JsonResponse
import json
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def emp_data_view(request):
    emp_data = {
        'eno': 100,
        'ename': 'Bhavani',
        'esal': 1000,
        'eaddr': 'sarvayaplli'
    }
    rep = '<h1>Employee Number:{}<br/>Employee Name:{}<br/>Employee Salary:{}<br/>Employee Address:{}</h1>'.format(
        emp_data['eno'], emp_data['ename'], emp_data['esal'], emp_data['eaddr'])
    return HttpResponse(rep)


def emp_data_jsonview(request):
    emp_data = {
        'eno': 100,
        'ename': 'Bhavani',
        'esal': 1000,
        'eaddr': 'sarvayaplli'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type='application/json')


def emp_data_jsonview2(request):
    emp_data = {
        'eno': 100,
        'ename': 'Bhavani',
        'esal': 1000,
        'eaddr': 'sarvayaplli'
    }

    return JsonResponse(emp_data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        emp_data = {
            'eno': 100,
            'ename': 'Subbu',
            'esal': 2000,
            'eaddr': 'Mydukur',

        }
        return JsonResponse(emp_data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is get Method'})
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is post Method'})
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is put Method'})
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is delete Method'})
        return HttpResponse(json_data, content_type='application/json')
