from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employee, Leave
import datetime
from django.db.models import Sum

def index(request):
    employees = Employee.objects.all()
    left_leaves = {}
    for employee in employees:
        left_leave = employee.givenLeave - employee.usedLeave
        left_leaves[employee.name] = left_leave
    context = {
    'employees':employees,
    'left_leaves':left_leaves,
    }
    return render(request, "leave/index.html", context)


def detail(request):
    leaves = Leave.objects.all()
    employees = Employee.objects.all()

    q = request.GET.get('q', '')
    if q:
        searched_employee = employees.get(name__icontains=q)
        search_key = searched_employee.id
        leaves = leaves.filter(employee_id=search_key).order_by('-updated_at')
    context = {
    'leaves':leaves,
    'q':q,
    }
    return render(request, "leave/detail.html", context)
