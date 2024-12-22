from django.db import models

# Create your models here. 

class Customer(models.Model):
    cname=models.CharField(max_length=100) 
    c_id=models.IntegerField(primary_key=True) 
    phone_no=models.IntegerField()  
class Product(models.Model):
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE) 
    pname=models.CharField(max_length=100) 
    p_id=models.IntegerField(primary_key=True)  
    price=models.IntegerField()
   
