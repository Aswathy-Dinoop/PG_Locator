from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=10,null=True)
class Registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True) 
    password=models.CharField(max_length=50,null=True)
class OwnerRegistration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True) 
    location=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
class ADD_PG_INFO(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    pgowner=models.ForeignKey(OwnerRegistration,on_delete=models.CASCADE,null=True)
    appartment_name=models.CharField(max_length=50,null=True)
    location=models.CharField(max_length=50,null=True) 
    facilities=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True) 
    price=models.CharField(max_length=50,null=True)
    image=models.ImageField(max_length=50,null=True) 
    transport=models.CharField(max_length=50,null=True)
    food=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=50,null=True)
    payment=models.CharField(max_length=50,null=True)

class AddtoCart(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    pg_info=models.ForeignKey(ADD_PG_INFO,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='media/',null=True)
    price=models.CharField(max_length=150,null=True)
    status=models.CharField(max_length=150,null=True)
    payment=models.CharField(max_length=150,null=True)