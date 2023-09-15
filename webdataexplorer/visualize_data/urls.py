from django.contrib import admin
from django.urls import path
from .views import VisualizeView

urlpatterns = [
    path('data/', VisualizeView.as_view(), name='visualize data'),
]