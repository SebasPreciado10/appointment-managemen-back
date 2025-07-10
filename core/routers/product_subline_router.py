from django.urls import path
from core.views.product_subline_view import (
    ProductSublineCreateView,
    ProductSublineListView,
    ProductSublineUpdateView,
    ProductSublineDeleteView,
)

urlpatterns = [
    path("product-sublines/create/", ProductSublineCreateView.as_view(), name="product-subline-create"),
    path("product-sublines/list/", ProductSublineListView.as_view(), name="product-subline-list"),
    path("product-sublines/update/", ProductSublineUpdateView.as_view(), name="product-subline-update"),
    path("product-sublines/delete/", ProductSublineDeleteView.as_view(), name="product-subline-delete"),
]
