from django.db import models
from cars.models import Car
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    