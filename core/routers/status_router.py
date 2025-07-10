from django.urls import path
from core.views.status_view import (
    StatusCreateView,
    StatusListView,
    StatusUpdateView,
    StatusDeleteView,
)

urlpatterns = [
    path("status/create/", StatusCreateView.as_view(), name="status-create"),
    path("status/list/", StatusListView.as_view(), name="status-list"),
    path("status/update/", StatusUpdateView.as_view(), name="status-update"),
    path("status/delete/", StatusDeleteView.as_view(), name="status-delete"),
]
