from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):  # type: ignore
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  # type: ignore
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):  # type: ignore
        return self.name
