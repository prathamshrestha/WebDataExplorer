from .models import Product, Vendor, Category
from django.http import HttpResponseBadRequest, JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class ScrapePostView(View):
    def post(self, request, *args, **kwargs):
        body = request.POST

        # Extract vendor and category data from the request
        vendor_name = body.get("vendor")
        category_name = body.get("category")

        if not vendor_name or not category_name:
            return HttpResponseBadRequest("Vendor and category are required fields.")


        # Create or retrieve vendor and category instances
        vendor, vendor_created = Vendor.objects.get_or_create(vendor_name=vendor_name)
        category, category_created = Category.objects.get_or_create(category_name=category_name)

        name = body.get("name")
        rating = body.get("rating")
        price = body.get("price")
        reviews = body.get("reviews")
        sold_by = body.get("sold_by")

        # Create a new Product instance
        Product.objects.create(
            name=name,
            vendor=vendor,
            rating=rating,
            price=price,
            reviews=reviews,
            sold_by=sold_by,
            category=category,
        )
        return JsonResponse({"message":"Data Posted"}, status = 201)


class VisualizeView(View):
    def get(self, request, *args, **kwargs):
        # Retrieve all product data
        data = Product.objects.all()
        return render(request, "visualize.html", {"data": data})
