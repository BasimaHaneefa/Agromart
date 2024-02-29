from django.db import models
from Admin.models import Subadmin,SProductType


# Create your models here.



class Products(models.Model): 
    product_name=models.CharField(max_length=100) 
    product_description=models.TextField(null=True) 
    product_image=models.FileField(upload_to='productimg/')
    product_rate=models.CharField(max_length=100)
    product_date=models.DateField(auto_now=True)
    producttype=models.ForeignKey(SProductType,on_delete=models.SET_NULL,null=True)
    subadmin=models.ForeignKey(Subadmin,on_delete=models.SET_NULL,null=True)


class ProductStock(models.Model): 
    product_stock=models.CharField(max_length=100) 
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)

class ProductGallery(models.Model): 
    productgallery_image=models.FileField(upload_to='productimg/') 
    product=models.ForeignKey(Products,on_delete=models.SET_NULL,null=True)