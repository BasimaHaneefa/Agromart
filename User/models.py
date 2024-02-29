from django.db import models
from Guest.models import *
from Farmer.models import *


# Create your models here.

class Sendrequest(models.Model):
    content=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(FarmerProducts,on_delete=models.SET_NULL,null=True)
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)
    payment_sts=models.IntegerField(default=0)
    req_date=models.DateField(auto_now=True,null=True)






    
