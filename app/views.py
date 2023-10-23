from django.shortcuts import render, redirect
from .form import *
from .models import *


# Create your views here.
def create(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('create')
    else:
        fm = StudentForm()
        data = Student.objects.all()
    return render(request, "index.html", {"fm": fm, 'data':data})


# Read data from database
def read(request):
    data = Student.objects.all()
    return render(request, 'index.html', {'data': data})


def edit(request, id):
    data_get = Student.objects.get(id=id)
    data = Student.objects.all()
    fm = StudentForm(instance=data_get)
    if request.method == "POST":
        fm = StudentForm(request.POST, instance=data_get)
        if fm.is_valid():
            fm.save()
            return redirect('create')
    return render(request, 'index.html', {'fm': fm, 'data': data})


def delete(request, id):
    dataget = Student.objects.get(id=id)
    dataget.delete()
    return redirect('create')
