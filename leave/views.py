from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from .models import Employee, Leave
import datetime
from django.db.models import Sum
from .forms import *

def index(request):
    today = datetime.date.today()
    employees = Employee.objects.all()
    for employee in employees:
        gap = today - employee.employed_date
        if gap.days // 365 >= 3:
             employee.givenLeave = 15 + ((gap.days // 365 - 3) // 2 + 1)
        pk = employee.id
        leaves = Leave.objects.filter(employee_id=pk)

        sum = 0
        for leave in leaves:
            sum += leave.leaveLen
        employee.usedLeave = sum
        employee.leftLeave = employee.givenLeave - employee.usedLeave
        employee.save()

    context = {
    'employees':employees,
    }

    return render(request, "leave/index.html", context)


def detail(request):
    leaves = Leave.objects.all()
    employees = Employee.objects.all()

    for leave in leaves:
        leaveGap = leave.endDate - leave.startDate
        leave.leaveLen = leaveGap.days
        if leave.endTime == '오전' and leave.startTime == '오후':
            pass
        elif leave.endTime == '오후' and leave.startTime == '오전':
            leave.leaveLen += 1
        else:
            leave.leaveLen += 0.5

        leave.save()

    q = request.GET.get('q', '')
    if q:
        try:
            searched_employee = employees.get(name__icontains=q)
        except:
            raise Http404("올바른 검색어를 입력해주세요")
        search_key = searched_employee.id
        leaves = leaves.filter(employee_id=search_key).order_by('-updated_at')
    context = {
    'leaves':leaves,
    'q':q,
    }
    return render(request, "leave/detail.html", context)


def regist(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == "POST":
        form = RegistForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = employee
            leave.save()
            return redirect('../../detail')
    else:
        form = RegistForm()

    return render(request, 'leave/regist.html', {'form': form})


def late_cal(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.late += 1
    employee.save()
    return redirect("../../leave")

def delete(request, pk):
    leave = Leave.objects.get(pk=pk)
    leave.delete()
    return redirect("../../leave/detail")

def edit(request, pk):
    leave = Leave.objects.get(pk=pk)
    if request.method == "POST":
        form = RegistForm(request.POST, instance=leave)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.save()
            return redirect('../../leave/detail')
    else:
        form = RegistForm(instance=leave)

    return render(request, 'leave/regist.html', {'form': form})
