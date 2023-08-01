from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=50)
    price =models.IntegerField()
    img = models.CharField(max_length=10000,null=True)
class User(models.Model):
    username = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=20)