from django.urls import path
# from .views import ProductDetailView, ProductListView
from .views import product_list, product_detail, manufacturer_list, manufacturer_detail


urlpatterns = [

    # path("", ProductListView.as_view(), name="products-list"),
    # path("products/<int:pk>", ProductDetailView.as_view(), name="products-detail")
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
    path("manufacturers/", manufacturer_list, name="manufacturer_list"),
    path("manufacturers/<int:pk>/", manufacturer_detail, name="manufacturer_detail")
]
