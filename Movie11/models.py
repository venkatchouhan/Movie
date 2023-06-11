from django.db import models

# Create your models here.
class Audience(models.Model):
    name = models.CharField(max_length=50)
    seat=models.IntegerField()
    price = models.IntegerField()