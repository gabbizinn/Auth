from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=200, null=True)
    student_name = models.CharField(max_length=200, null=True)
    student_contact = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.student_name


# class Customer(models.Model):
#     name= models.CharField(max_length=200,null=True)
#     phone= models.CharField(max_length=200,null=True)
#     email= models.CharField(max_length=200,null=True)
#     date= models.DateTimeField(auto_now_add=True,null=True)

#     # This string value is so I can see the value(name) of the customer
#     def __str__(self):
#         return self.name

# class Product(models.Model):
#     CATEGORY = (
#         ("Boy","Boy" ),
#         ("Girl","Girl" ),
#     )
#     name= models.CharField(max_length=200,null=True)
#     price= models.FloatField(null=True)
#     category= models.CharField(max_length=200,null=True, choices=CATEGORY)
#     description= models.CharField(max_length=200,null=True, blank=True)
#     date= models.DateTimeField(auto_now_add=True,null=True)
    
# class Order(models.Model):
#     STATUS = (
#         ("Orders in the making","Orders in the making" ),
#         ("Out for delivery", "Out for delivery"),
#         ("Order delivered","Order delivered"),
#     )
#     customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
#     product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL) 
#     date= models.DateTimeField(auto_now_add=True,null=True)
#     status= models.CharField(max_length=200,null=True, choices=STATUS)

#     # This string value is so I can see the value(name) of the order
#     def __str__(self):
#         return self.product.name
