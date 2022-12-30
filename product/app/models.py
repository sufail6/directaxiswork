from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    category_id = models.CharField(max_length=25, null=True)
    price = models.IntegerField()


class Category(models.Model):
    category_name = models.CharField(max_length=50)


def product():
    return None