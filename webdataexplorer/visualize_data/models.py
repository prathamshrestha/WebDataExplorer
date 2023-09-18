from django.db import models
from django.core.exceptions import ValidationError

def validate_rating(value):
    if value < 0 or value > 5:
        raise ValidationError('Rating must be between 0 and 5.')

class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=255, default="Vendor", verbose_name='vendor name')

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
        ordering = ['id', ]

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255, default="Category")

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id', ]

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, default="Item")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[validate_rating])
    price = models.CharField(max_length=255, blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    sold_by = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id', ]

    def __str__(self):
        return str(self.id) + ". " + self.name
