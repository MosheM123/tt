from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
import django.contrib.postgres.fields


# Create your models here.
class Customer(AbstractUser):
    username = models.CharField(max_length=255, unique=True, default='s')
    password = models.CharField(max_length=255, default='s')
    email = models.CharField(max_length=255, default='s')
    last_login = models.CharField(max_length=255, default='s')

    def __str__(self):
        return self.username


class Products(models.Model):
    itsname = models.CharField(max_length=255)
    price = models.IntegerField()
    img = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, default='ss')
    age = models.IntegerField(default=12)
    img2 = models.CharField(max_length=255, default='ebe')
    img3 = models.CharField(max_length=255, default='ee')

    def __str__(self):
        return self.itsname


class Products_Sale(models.Model):
    itsname = models.CharField(max_length=255)
    price = models.IntegerField()
    img = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, default='ss')
    age = models.IntegerField(default=12)
    img2 = models.CharField(max_length=255, default='ebe')
    img3 = models.CharField(max_length=255, default='ee')

    def __str__(self):
        return self.itsname


class All_Products(models.Model):
    itsname = models.CharField(max_length=255)
    price = models.IntegerField()
    img = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, default='ss')
    age = models.IntegerField(default=12, unique=False)
    img2 = models.CharField(max_length=255, default='ebe')
    img3 = models.CharField(max_length=255, default='ee')

    def __str__(self):
        return self.itsname


class Personal_cart(models.Model):
    quantity = models.IntegerField(default=0)
    board = ArrayField(
        models.IntegerField(
            max_length=10,
            blank=True
        ),
        size=8,
        default = [-1]
    )


class Cart_item(models.Model):
    item = models.ForeignKey(All_Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.item
