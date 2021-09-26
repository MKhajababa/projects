from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import EmailField
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    is_agent = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)


class AgentUser(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE,primary_key = True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(null=False,blank=False,default = None)
    pic = models.ImageField(blank=True, null=True, upload_to='images/')
    is_available = models.BooleanField(default = False)
	


class CustomerUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    pic = models.ImageField(blank=True, null=True, upload_to='images/')


class LeadDetails(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone =  PhoneNumberField(null=False,blank=False,default =None)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=150)
    occupation = models.CharField(max_length=20)
    agent = models.ForeignKey(AgentUser, on_delete=models.DO_NOTHING,default = None)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    describtion = models.CharField(max_length=200)


class FeedBack(models.Model):
    discribtion = models.TextField()
    email = models.EmailField(unique=True)
