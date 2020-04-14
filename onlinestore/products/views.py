from django.shortcuts import render
from django.http import JsonResponse

from .models import Manufacturer, Product


def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        products = Product.objects.get(pk=pk)
        data = {"Product": {
                            "name": products.name,
                            "manufacturer": products.manufacturer.name,
                            "description": products.description,
                            "photo": products.photo.url,
                            "price": products.price,
                            "shipping_cost": products.shipping_cost,
                            "quantity": products.quantity,
                            }
                }
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                    "code": 404,
                    "message": "Product is Not Found"}
        }, status=404)
    return response


def manufacturer_list(request):
    manufacturer = Manufacturer.objects.filter(active=True)
    data = {"manufacturer": list(manufacturer.values())
            }
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {"Manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
            "products": list(manufacturer_products.values())
        }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Manufacturer does not exist"
            }}, status=404)
    return response

# from django.views.generic import DetailView, ListView
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/product_list.html'





