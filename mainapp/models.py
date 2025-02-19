from django.db import models

# Create your models here.
class Users(models.Model):
    full_name=models.CharField(max_length=150)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=64)
    def __str__(self):
        return self.full_name