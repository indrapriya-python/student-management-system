from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from . models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,"dashboard.html")





def courses(request):
    course = Courses.objects.all()
    return render(request,"courses.html",{'course':course})

def addcourses(request):
    if request.method == 'POST':
        course_name = request.POST.get('courseename')
        fees = request.POST.get('fees')
        duration = request.POST.get('duraction')
        Courses.objects.create(course_name=course_name,fees = fees, duration = duration)
        return redirect('/courses/')
        






def signup(request):
    return render(request,"sign-up.html")

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        if User.objects.filter(email=email).exists():
            messages.error(request, "email Already exists")
            return redirect("/signup/")
        
        else:
            User.objects.create(name=name,email=email,password=password)
            return redirect("/dashboard/")
        

def tables(request):
    return render(request,"tables.html")


def viewstudents(request):
    return render(request,"viewstudents.html")

