from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path("", include("core.routers.appointment_router")),
    path("", include("core.routers.supplier_router")),
    path("", include("core.routers.product_subline_router")),
    path("", include("core.routers.status_router")),
    path("", include("core.routers.report_router")),
]
