from django.db import models


# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class District(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Place(models.Model):
    name=models.CharField(max_length=50) 
    district=models.ForeignKey(District,on_delete=models.CASCADE)      

class Subadmin(models.Model):
    name=models.CharField(max_length=50)  
    contact=models.CharField(max_length=50)    
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    photo=models.FileField(upload_to='UserPhoto/')
    password=models.CharField(max_length=50)
    confirmpassword=models.CharField(max_length=50) 

class Feedback(models.Model):
    feedback=models.CharField(max_length=6000)
    user=models.ForeignKey("Guest.User",on_delete=models.SET_NULL,null=True)
    farmer=models.ForeignKey("Guest.Farmer",on_delete=models.SET_NULL,null=True)
    market=models.ForeignKey("Guest.Market",on_delete=models.SET_NULL,null=True)

class Complaint(models.Model):
    complaint=models.CharField(max_length=6000)
    user=models.ForeignKey("Guest.User",on_delete=models.SET_NULL,null=True)
    farmer=models.ForeignKey("Guest.Farmer",on_delete=models.SET_NULL,null=True)
    market=models.ForeignKey("Guest.Market",on_delete=models.SET_NULL,null=True)
    status=models.IntegerField(default=0)
    reply=models.CharField(max_length=5000,default="Not Yet Viewed")

class SProductType(models.Model):
    producttype_name=models.CharField(max_length=50)

    def __str__(self):
        return self.producttype_name
    



