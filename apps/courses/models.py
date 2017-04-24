from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=225)
    description=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    
