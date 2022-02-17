from django.db import models

# Create your models here.


class Product(models.Model):
    # blank = if it can our cant be left with out any info in it
    # null = if its ins empty how the database will safe that information

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    sumary = models.TextField(default='capivara')
    feature = models.BooleanField()  # null=True, blank=True
