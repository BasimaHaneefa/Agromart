from django.db import models
from Guest.models import Farmer,Market
from Subadmin.models import Products
from Market.models import Marketevent


#Create your models here.

class ProductType(models.Model):
    product_type=models.CharField(max_length=50)       

    def __str__(self):
        return self.product_type

class FarmerProducts(models.Model):
    name=models.CharField(max_length=50)
    details=models.CharField(max_length=50)
    photo=models.FileField(upload_to='ProductPhoto/')
    ptype=models.ForeignKey(ProductType,on_delete=models.SET_NULL,null=True)
    rate=models.CharField(max_length=50)
    farmer=models.ForeignKey(Farmer,on_delete=models.SET_NULL,null=True)

class Stock(models.Model):
    date=models.DateField(auto_now_add=True)
    quantity=models.CharField(max_length=50)  
    product=models.ForeignKey(FarmerProducts,on_delete=models.SET_NULL,null=True) 
    

class farmerRequest(models.Model):
    content=models.CharField(max_length=500)
    farmer=models.ForeignKey(Farmer,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(FarmerProducts,on_delete=models.SET_NULL,null=True)
    market=models.ForeignKey(Market,on_delete=models.SET_NULL,null=True)
    status=models.IntegerField(default=0)



class Request(models.Model):
    quantity=models.CharField(max_length=50)
    req_date=models.DateField(auto_now=True)
    total_amnt=models.CharField(max_length=50)
    req_sts=models.IntegerField(default=0)
    p_sts=models.IntegerField(default=0)
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)
    farmer=models.ForeignKey(Farmer,on_delete=models.SET_NULL,null=True)
    req_date=models.DateField(auto_now=True,null=True)



class AuctionSlotBooking(models.Model):
    marketevent=models.ForeignKey(Marketevent,on_delete=models.SET_NULL,null=True)
    farmer=models.ForeignKey(Farmer,on_delete=models.SET_NULL,null=True)
    slotbookdate=models.DateField(auto_now=True)
    slotbooktime=models.TimeField(auto_now=True)
    slot_status=models.IntegerField(default=0)


class SlotReply(models.Model):
    slotbook=models.ForeignKey(AuctionSlotBooking,on_delete=models.SET_NULL,null=True)
    slotreply_no=models.CharField(max_length=50)
    slotreply_allocatetime=models.CharField(max_length=50)
    