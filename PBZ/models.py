from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    company = models.CharField(max_length=100)


class Customer(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    passport_id = models.IntegerField()
    passport_series = models.CharField(max_length=2)
    bank_details = models.CharField(max_length=100)


class Destination(models.Model):
    country = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.IntegerField()
    flat_number = models.IntegerField()


class Waybill(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    current_price = models.FloatField()
    date= models.DateField()
    number_of_product = models.IntegerField()
    destination = models.OneToOneField(Destination, on_delete=models.CASCADE)

# Create your models here.
