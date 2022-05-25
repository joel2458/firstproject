from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True)
    user_address = models.TextField(max_length=100)
    user_gender = models.CharField(max_length=100)    
    user_image = models.ImageField(upload_to="image/", null=True)

class course(models.Model):
    course_name = models.CharField(max_length=225)
    fee = models.IntegerField()



class student(models.Model):
    course = models.ForeignKey(course, on_delete=models.CASCADE, null=True)
    std_name =models.CharField(max_length=225)
    std_address =models.CharField(max_length=225)
    std_age =models.IntegerField()
    Join_date =models.DateField()

