from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)


class ProductMod(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    guid = models.CharField(name='guid', max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=100)
    isDrink = models.BooleanField(name='drink', default=True)
    guid = models.CharField(name='guid', max_length=50)


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer)
    timestamp = models.DateTimeField(name='order_timestamp')
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()


class OrderItem_Mods(models.Model):
    orderItem = models.ForeignKey(OrderItem)
    mod = models.ForeignKey(ProductMod)
    quantity = models.IntegerField()
