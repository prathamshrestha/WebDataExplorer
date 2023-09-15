from django.db import models	

class DarazModel(models.Model):
    sn = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=255, default="Item")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=1.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True)
    sold_by = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.sn) + ". " + self.name
    
# class Model(models.Model):
#     sn = models.IntegerField(primary_key=True)

#     name = models.CharField(max_length=200, default="Item")
#     rating = models.CharField(max_length=20, blank=True, Null=True)
#     price = models.CharField(max_length=20, blank=True, Null=True)
#     reviews = models.CharField(max_length=20, blank=True, Null=True)
#     sold_by = models.CharField(max_length=20, blank=True, Null=True)
#     category = models.CharField(max_length=20, blank=True, Null=True)
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return str(self.sn) + ". " + self.name
