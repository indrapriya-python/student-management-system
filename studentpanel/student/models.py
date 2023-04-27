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

    