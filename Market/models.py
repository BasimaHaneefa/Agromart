from django.db import models

from Guest.models import Market
from Admin.models import*

# Create your models here.
class Marketevent(models.Model):
    market=models.ForeignKey(Market,on_delete=models.CASCADE)
    marketevent_date=models.DateField()
    marketevent_starttime=models.TimeField()
    marketevent_description=models.TextField(null=True)
    