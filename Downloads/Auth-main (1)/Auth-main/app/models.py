from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True) #if you want to go back and change this in your database or if the user doesn't have all of the options
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self): #This is so I don't see (object 1) I see the customer name
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null = True)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    STATUS= (
        ("Making label","Making label"),
        ("Out for delivery", "Out for delivery"),
        ("Pending"),
    )
    # customer = 
    # product = 
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True)

