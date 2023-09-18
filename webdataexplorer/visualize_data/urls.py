from django.urls import path
from .views import VisualizeView, ScrapePostView


urlpatterns = [
    path("scrape_data_list/", VisualizeView.as_view(), name="visualize data"),
    path("api/item/", ScrapePostView.as_view(), name="create data"),
]
