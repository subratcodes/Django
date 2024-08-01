from django.db import models


class Discount(models.Model): 
    discount=models.IntegerField(default=100)

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=False,default="Some text")
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)



