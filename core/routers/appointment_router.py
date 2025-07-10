from django.urls import path
from core.views.appointment_view import (
    AppointmentCreateView,
    AppointmentListView,
    AppointmentUpdateView,
    AppointmentReadView,
    AppointmentCancelView,
)

urlpatterns = [
    path("appointments/create/", AppointmentCreateView.as_view(), name="appointment-create"),
    path("appointments/list/", AppointmentListView.as_view(), name="appointment-list"),
    path("appointments/update/<uuid:id>/", AppointmentUpdateView.as_view(), name="appointment-update"),
    path("appointments/read/<uuid:id>/", AppointmentReadView.as_view(), name="appointment-read"),
    path("appointments/delete/<uuid:id>/", AppointmentCancelView.as_view(), name="appointment-delete"),
]