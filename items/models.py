from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=3, default='usd')

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)

    def get_total_cost(self):
        return sum(item.price for item in self.items.all())


class Discount(models.Model):
    name = models.CharField(max_length=255)
    percent_off = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
