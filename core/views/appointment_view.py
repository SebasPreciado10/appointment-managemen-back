from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_spectacular.utils import extend_schema

from core.serializers.appointment_serializer import AppointmentCreateSerializer, AppointmentResponseSerializer,AppointmentUpdateSerializer
from core.services.appointment_service import create_appointment
from core.exceptions.appointment_exceptions import AppointmentAlreadyExists
from core.services.appointment_service import list_appointments, update_appointment, cancel_appointment, get_appointment
from core.exceptions.appointment_exceptions import AppointmentNotFound
from drf_spectacular.utils import OpenApiParameter



@extend_schema(tags=["Appointments"], summary="Crear una nueva cita", description="Crea una cita de entrega con proveedor, sublínea, estado y detalles opcionales.", request=AppointmentCreateSerializer, responses={201: AppointmentResponseSerializer})
class AppointmentCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = AppointmentCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                appointment = create_appointment(serializer.validated_data, request.user)
                response_serializer = AppointmentResponseSerializer(appointment)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            except AppointmentAlreadyExists as e:
                return Response({"detail": str(e.detail)}, status=e.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Appointments"], summary="Listar citas", parameters=[
    OpenApiParameter("supplier", str, required=False),
    OpenApiParameter("product_subline", str, required=False),
    OpenApiParameter("status", str, required=False),
    OpenApiParameter("date_from", str, required=False),
    OpenApiParameter("date_to", str, required=False),
], responses={200: AppointmentResponseSerializer(many=True)})
class AppointmentListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        appointments = list_appointments(request.query_params)
        serializer = AppointmentResponseSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@extend_schema(
    tags=["Appointments"],
    summary="Leer cita",
    responses={200: AppointmentResponseSerializer}
)
class AppointmentReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        try:
            appointment = get_appointment(id)
            serializer = AppointmentResponseSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AppointmentNotFound as e:
            return Response({"detail": str(e.detail)}, status=e.status_code)




@extend_schema(tags=["Appointments"], summary="Actualizar cita", request=AppointmentUpdateSerializer, responses={200: AppointmentResponseSerializer})
class AppointmentUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, id):
        data = request.data
        data['id'] = id 
        serializer = AppointmentUpdateSerializer(data=data)

        if serializer.is_valid():
            try:
                appointment = update_appointment(serializer.validated_data)
                response_serializer = AppointmentResponseSerializer(appointment)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except AppointmentNotFound as e:
                return Response({"detail": str(e.detail)}, status=e.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["Appointments"],
    summary="Cancelar cita",
    parameters=[
        OpenApiParameter("id", str, required=True, location=OpenApiParameter.PATH),
    ],
    responses={200: AppointmentResponseSerializer},
)
class AppointmentCancelView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        try:
            appointment_id = kwargs.get("id") 
            appointment = cancel_appointment(appointment_id)
            serializer = AppointmentResponseSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AppointmentNotFound as e:
            return Response({"detail": str(e.detail)}, status=e.status_code)
