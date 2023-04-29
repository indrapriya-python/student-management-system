from . models import *
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def index(request):
    return render(request, "index.html")


def dashboard(request):
    courses = Courses.objects.all()
    stu = Student.objects.all()
    cname = Courses.objects.all().count()
    stu_name = Student.objects.all().count()
    return render(request, "dashboard.html", {"courses":courses, 
                                              "stu":stu,
                                              "cname":cname,
                                              "stu_name":stu_name})


def courses(request):
    course = Courses.objects.all()
    return render(request, "courses.html", {'course': course})


def addcourses(request):
    if request.method == 'POST':
        course_name = request.POST.get('courseename')
        fees = request.POST.get('fees')
        duration = request.POST.get('duraction')
        Courses.objects.create(course_name=course_name,
                               fees=fees, duration=duration)
        return redirect('/courses/')


def signup(request):
    return render(request, "sign-up.html")


def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        if User.objects.filter(email=email).exists():
            messages.error(request, "email Already exists")
            return redirect("/signup/")

        else:
            User.objects.create(name=name, email=email, password=password)
            return redirect("/dashboard/")


def tables(request):
    return render(request, "tables.html")


def viewstudents(request):
    course = Courses.objects.all()
    student = Student.objects.all()
    return render(request, "viewstudents.html", {'course':course, 'student':student})


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        degree = request.POST.get('degree')
        course = request.POST.get('course')
        stu = Courses.objects.get(id = course)

        if Student.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
        elif Student.objects.filter(phone=phone).exists():
            messages.error(request,"Phone no already exists")
        else:    
            Courses.objects.create(name=name , email = email,phone=phone,college = college,degree=degree,course=course)
            return render(request, 'viewstudents.html', {'cource':cource})   



        
