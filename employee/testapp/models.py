from django.db import models

# Create your models here.
class Employee(models.Model):
  eno=models.IntegerField()
  ename=models.CharField(max_length=25)
  esal=models.FloatField()
  eddar=models.CharField(max_length=200)
def __str__(self):
  return 'Employee Object eno:+str(self.no)'

