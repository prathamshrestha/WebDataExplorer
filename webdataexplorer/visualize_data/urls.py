from django.contrib import admin
from django.urls import path
from .views import VisualizeView, ScrapePostView


# TODO: 3. READme make more clear about the purpose of the project
urlpatterns = [
    path("scrape_data_list/", VisualizeView.as_view(), name="visualize data"),
    path("api/create/", ScrapePostView.as_view(), name="create data"),
]
