from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)