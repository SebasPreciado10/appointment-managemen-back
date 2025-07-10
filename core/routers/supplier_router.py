from django.urls import path
from core.views.supplier_view import (
    SupplierCreateView,
    SupplierListView,
    SupplierUpdateView,
    SupplierDeleteView,
)

urlpatterns = [
    path("suppliers/create/", SupplierCreateView.as_view(), name="supplier-create"),
    path("suppliers/list/", SupplierListView.as_view(), name="supplier-list"),
    path("suppliers/update/", SupplierUpdateView.as_view(), name="supplier-update"),
    path("suppliers/delete/<uuid:id>/", SupplierDeleteView.as_view(), name="supplier-delete"),
]
