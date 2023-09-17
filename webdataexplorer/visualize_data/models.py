from django.db import models


class DarazModel(models.Model):
    sn = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=255, default="Item")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    price = models.CharField(max_length=255, blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    sold_by = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sn) + ". " + self.name
