from django import forms
from .models import Product  # Import your model here

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'vendor', 'rating', 'price', 'reviews', 'sold_by', 'category']
