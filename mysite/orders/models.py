from django.db import models
from users.models import User
# Create your models here

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.CharField(max_length=100)
    price = models.IntegerField()

    

