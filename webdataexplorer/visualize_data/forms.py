from django import forms
from .models import DarazModel  # Import your model here

class DarazModelForm(forms.ModelForm):
    class Meta:
        model = DarazModel
        fields = ['name', 'rating', 'price', 'reviews', 'sold_by', 'category']
