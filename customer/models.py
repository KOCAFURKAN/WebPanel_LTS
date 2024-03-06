from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)

class Dept(models.Model):
    amount=models.FloatField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Payment(models.Model):
    amount=models.FloatField()
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)        