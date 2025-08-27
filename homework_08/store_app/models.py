from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        related_name="product",
        null=True,
    )


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
