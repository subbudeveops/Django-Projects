from django.db import models
import datetime
# Create your models here.
class Post(models.Model):
  Male='M'
  FeMale='F'
  GENDER_CHOICE=((Male,'Male'),(FeMale,'female'))
  name=models.CharField(max_length=20,blank=False,null=False)
  text=models.TextField(blank=False,null=False)
  gender=models.CharField(max_length=6,choices=GENDER_CHOICE)
  time=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
    