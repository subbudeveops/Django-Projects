from django.db import models

# Create your models here.


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=20)
    esal = models.FloatField()
    eaddress = models.CharField(max_length=200)
