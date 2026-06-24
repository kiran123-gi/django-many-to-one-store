from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=100)
    price = models.FloatField()
    procust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.pname}"
