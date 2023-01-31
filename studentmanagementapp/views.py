from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from studentmanagementapp.models import City, Course, Student


# Create your views here.
def reg_fun(request):
    return render(request, 'register.html', {'data': ''})


def regdata_fun(request):
    user_name = request.POST['txtuser']
    user_email = request.POST['tbemail']
    user_password = request.POST['tbpass']

    if User.objects.filter(Q(username= user_name) | Q(email=user_email)).exists():
        return render(request, 'register.html', {'data': 'Username,email and password already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_password)
        u1.save()
        return redirect('log')


def log_fun(request):
    return render(request, 'login.html', {'data': ''})


def home_fun(request):
    return render(request, 'home.html')


def logdata_fun(request):
    user_name = request.POST['txtusername']
    user_password = request.POST['tbpassword']
    user1 = authenticate(username=user_name, password=user_password)
    if user1 is not None:
        if user1.is_superuser:
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'data': 'User is not a superuser'})
    else:
        return render(request, 'login.html', {'data': 'Enter proper username and password'})


def addstudents_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request, 'addstudent.html', {'City_Data': city, 'Course_Data': course})


def reddata_fun(request):
    s1 = Student()
    s1.Std_Name = request.POST['txtname']
    s1.Std_Age = request.POST['txtage']
    s1.Std_Phno = request.POST['txtphn']
    s1.Std_City = City.objects.get(City_Name=request.POST['ddlcity'])
    s1.Std_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
    s1.save()
    return redirect('add')


def display_fun(request):
    s1 = Student.objects.all()
    return render(request, 'display.html', {'data': s1})


def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()

    if request.method == 'POST':
        s1.Std_Name = request.POST['txtname']
        s1.Std_Age = request.POST['txtage']
        s1.Std_Phno = request.POST['txtphn']
        s1.Std_City = City.objects.get(City_Name=request.POST['ddlcity'])
        s1.Std_Course = Course.objects.get(Course_Name=request.POST['ddlcourse'])
        s1.save()
        return redirect('display')

    return render(request, 'update.html', {'data': s1, 'City_Data': city, 'Course_Data': course})


def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')


def log_out_fun(request):
    return redirect('log')