from django.contrib import admin
from django.urls import path
from .views import VisualizeView, daraz_data_post

urlpatterns = [
    path("data/", VisualizeView.as_view(), name="visualize data"),
    path("create/", daraz_data_post, name="create data"),
]
