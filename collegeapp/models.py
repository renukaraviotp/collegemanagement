from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    coursename = models.CharField(max_length=255)
    coursefee  = models.CharField(max_length=255)

class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255)
    age = models.IntegerField() 
    contactnumber = models.CharField(max_length=255)
    joindate = models.DateField() 
    gender = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/') 

class Student(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    joindate = models.DateField()
    qualification = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)