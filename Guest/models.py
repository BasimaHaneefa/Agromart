from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class Login(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Market(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    address=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    logo=models.FileField(upload_to='Userlogo/')
    proof=models.FileField(upload_to='Userproof/')
    password=models.CharField(max_length=50,unique=True)
    confirmpassword=models.CharField(max_length=50)
    status=models.IntegerField(default=0)

class Farmer(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    photo=models.FileField(upload_to='UserPhoto/')
    password=models.CharField(max_length=50,unique=True)
    confirmpassword=models.CharField(max_length=50)
    
class User(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField(unique=True,null=True)
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.SET_NULL,null=True)
    photo=models.FileField(upload_to='UserPhoto/')
    password=models.CharField(max_length=50,unique=True)
    confirmpassword=models.CharField(max_length=50)
    

    
class Admin(models.Model): 
    name=models.CharField(max_length=100,null=True) 
    email=models.CharField(max_length=100) 
    password=models.CharField(max_length=50)