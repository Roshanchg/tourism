from django.db import models
from django.utils import timezone
# Create your models here.
class Users(models.Model):
    full_name=models.CharField(max_length=150)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=64)
    def __str__(self):
        return self.full_name

class Destinations(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    favcount=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Rating(models.IntegerChoices):
    ONE_STAR = 1, 'One Star'
    TWO_STAR = 2, 'Two Stars'
    THREE_STAR = 3, 'Three Stars'
    FOUR_STAR = 4, 'Four Stars'
    FIVE_STAR = 5, 'Five Stars'


class Reviews(models.Model):
    destination=models.ForeignKey(Destinations,on_delete=models.CASCADE)
    stars=models.IntegerField(choices=Rating.choices, default=Rating.FIVE_STAR)
    text=models.CharField(max_length=1000)
    dateofreview=models.DateField(default=timezone.now)
    userID=models.ForeignKey(Users,on_delete=models.CASCADE)

class UserArchive(models.Model):
    userID=models.ForeignKey(Users,on_delete=models.CASCADE)
    destination=models.ForeignKey(Destinations,on_delete=models.CASCADE)
