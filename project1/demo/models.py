from django.db import models
from django.db.models import Model
import datetime
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=60)
    name=models.CharField(max_length=60)
    image=models.ImageField(upload_to="images/")
    desc=models.TextField()
    created_at=models.DateTimeField(default=datetime.datetime.now)

    

