from django.db import models

from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import EmailField
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    is_agent = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    pic = models.ImageField(blank=True, null=True, upload_to='images/')
    socialauth = models.BooleanField(default = True)

class AgentUser(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE,primary_key = True)
    phone_number = PhoneNumberField(null=False,blank=False,default = None)
    is_available = models.BooleanField(default = False)

    


class LeadDetails(models.Model):
    user = models.ForeignKey(User,on_delete = models.DO_NOTHING,default = None)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone =  PhoneNumberField(null=False,blank=False,default =None)
    email = models.EmailField()
    is_selected = models.BooleanField(default=False)
    is_v = models.BooleanField(default = True)
    address = models.CharField(max_length=150)
    occupation = models.CharField(max_length=20)
    agent = models.ForeignKey(AgentUser, on_delete=models.DO_NOTHING,default = None)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    describtion = models.CharField(max_length=200)

class VechileDetails(models.Model):
    lead = models.ForeignKey(LeadDetails,on_delete = models.CASCADE,default = None)
    license = models.CharField(max_length=15)
    licencepic = models.ImageField(blank=True, null=True, upload_to='images/')
    Rcpic = models.ImageField(blank=True, null=True, upload_to='images/')
    Rigestration_Number = models.CharField(max_length = 15,unique=True)
    licenseuser = models.CharField(max_length = 30)

    phone = PhoneNumberField(null=False,blank=False,default =None)

class ObjectDetails(models.Model):
    lead = models.ForeignKey(LeadDetails,on_delete = models.CASCADE,default = None)
    item_name = models.CharField(max_length=30)
    UID =models.CharField(max_length=20,unique = True)
    Pdate = models.DateTimeField(default = now)

class FeedBack(models.Model):
    discribtion = models.TextField()
    email = models.EmailField(unique=True)
