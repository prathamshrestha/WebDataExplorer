from .models import DarazModel
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views import View
from django.shortcuts import render
from .forms import DarazModelForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def daraz_data_post(request, *args, **kwargs):
    daraz_model = DarazModel.objects
    data = request.POST
    name = data.get('name')
    rating = data.get('rating')
    price = data.get('price')
    reviews = data.get('reviews')
    sold_by = data.get('sold_by')
    category = data.get('category')
    
    daraz_model.create(
        name=name,
        rating=rating,
        price=price,
        reviews=reviews,
        sold_by=sold_by,
        category=category
        )
    return HttpResponse('Data Posted')

class VisualizeView(View):
    def get(self, request, *args, **kwargs):
        data = DarazModel.objects.all() 
        return render(request, './visualize.html', {'data': data})

