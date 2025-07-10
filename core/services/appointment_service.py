from core.models.appointment import Appointment
from core.exceptions.appointment_exceptions import (
    AppointmentAlreadyExists,
    AppointmentNotFound
)
from core.models.status import Status
from uuid import UUID


def create_appointment(validated_data, user):
    scheduled = validated_data.get("scheduled_delivery")
    supplier = validated_data.get("supplier")
    product_subline = validated_data.get("product_subline")

    if Appointment.objects.filter(
        scheduled_delivery=scheduled,
        supplier=supplier,
        product_subline=product_subline
    ).exists():
        raise AppointmentAlreadyExists()

    return Appointment.objects.create(created_by_user=user, **validated_data)


def list_appointments(params):
    queryset = Appointment.objects.all()

    if supplier := params.get("supplier"):
        queryset = queryset.filter(supplier__id=supplier)
    if product_subline := params.get("product_subline"):
        queryset = queryset.filter(product_subline__id=product_subline)
    if status := params.get("status"):
        queryset = queryset.filter(status__id=status)
    if date_from := params.get("date_from"):
        queryset = queryset.filter(scheduled_delivery__date__gte=date_from)
    if date_to := params.get("date_to"):
        queryset = queryset.filter(scheduled_delivery__date__lte=date_to)

    return queryset.order_by("-scheduled_delivery")

def get_appointment(appointment_id: UUID):
    try:
        return Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        raise AppointmentNotFound()


def update_appointment(validated_data):
    appointment_id = validated_data.get("id")
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        raise AppointmentNotFound()

    for attr, value in validated_data.items():
        setattr(appointment, attr, value)

    appointment.save()
    return appointment


def cancel_appointment(appointment_id: UUID):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        raise AppointmentNotFound()

    try:
        cancelled_status = Status.objects.get(name__iexact="Cancelada")
    except Status.DoesNotExist:
        raise AppointmentNotFound(detail="El estado 'Cancelada' no está registrado.")

    appointment.status = cancelled_status
    appointment.save()
    return appointment
