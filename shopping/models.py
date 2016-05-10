from django.db import models

# Create your models here.


class User(models.Model):
    SEX = (("M", "male"), ("F", "female"))
    gender = models.CharField(max_length=30, choices=SEX, default="M")
    name = models.CharField(max_length=30)
    birthdate = models.DateField()
    email = models.EmailField(unique=True)
    home_num = models.CharField(max_length=40)
    phone_num = models.CharField(max_length=40)
    addr = models.CharField(max_length=100)
    addr_backup = models.CharField(max_length=100)
    info = models.TextField()
    is_exist = models.IntegerField(default=1)

