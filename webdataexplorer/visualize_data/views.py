from .models import DarazModel
from django.http import HttpResponse
from django.core import serializers
from django.views import View
from django.shortcuts import render
from .forms import DarazModelForm

class VisualizeView(View):
    def post(self, request, *args, **kwargs):
        form = DarazModelForm(request)
        if form.is_valid():
            form.save()
            render(request, './Scrape.html', form)
            
        
    def get(self, request, *args, **kwargs):
        return render(
            request=request, 
            template_name='./Scrape.html', 
            context={
                'form':DarazModelForm
                }
            )
