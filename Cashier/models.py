from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)


class ProductMod(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=100)
    isDrink = models.BooleanField(name='drink', default=True)
    guid = models.CharField(max_length=50)


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    timestamp = models.DateTimeField(name='order_timestamp')


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    mods = models.ForeignKey(ProductMod)
    quantity = models.IntegerField()

