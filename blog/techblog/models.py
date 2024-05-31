from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    cont = models.TextField()
    created_at=models.DateTimeField(default=datetime.now,blank=True)