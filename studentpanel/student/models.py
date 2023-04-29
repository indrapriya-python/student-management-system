from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=250)


class Courses(models.Model):
    course_name = models.CharField(max_length=200)
    fees = models.FloatField()
    duration = models.TextField()


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=10)
    collage = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
