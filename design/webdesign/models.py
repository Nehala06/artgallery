from django.db import models

# Create your models here.


class registration(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=10)
    passwordre=models.CharField(max_length=10)
