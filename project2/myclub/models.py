from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
  name=models.CharField('Venue name',max_length=100)
  address=models.CharField(max_length=100)
  zip_code=models.CharField('Zip code',max_length=10)
  phone=models.CharField('conatact number',max_length=14)
  web=models.URLField('website address')
  email_address=models.EmailField('Email address')
  def __str__(self):
    return self.name

class MyClubUser(models.Model):
  first_name=models.CharField(max_length=25)
  last_name=models.CharField(max_length=25)
  email=models.EmailField('User Email') 

  def __str__(self):
    return self.first_name


class Event(models.Model):
  name=models.CharField(max_length=200)
  event_date=models.DateTimeField()
  venue=models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
  manager=models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
  description=models.TextField(blank=True)
  attends=models.ManyToManyField(MyClubUser,blank=True)

  def __str__(self):
    return self.name
