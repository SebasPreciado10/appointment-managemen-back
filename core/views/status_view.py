from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_spectacular.utils import extend_schema, OpenApiParameter

from core.serializers.status_serializer import (
    StatusCreateSerializer,
    StatusResponseSerializer,
    StatusUpdateSerializer,
)
from core.services.status_service import (
    create_status,
    list_statuses,
    update_status,
    delete_status,
)
from core.exceptions.status_exceptions import (
    StatusAlreadyExists,
    StatusNotFound,
)


@extend_schema(tags=["Status"])
class StatusCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Crear un estado",
        request=StatusCreateSerializer,
        responses={201: StatusResponseSerializer},
    )
    def post(self, request):
        serializer = StatusCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                status_obj = create_status(serializer.validated_data)
                response_serializer = StatusResponseSerializer(status_obj)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            except StatusAlreadyExists as e:
                return Response({"detail": str(e.detail)}, status=e.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Status"])
class StatusListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Listar estados",
        responses={200: StatusResponseSerializer(many=True)},
    )
    def get(self, request):
        statuses = list_statuses()
        serializer = StatusResponseSerializer(statuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=["Status"])
class StatusUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Actualizar estado",
        request=StatusUpdateSerializer,
        responses={200: StatusResponseSerializer},
    )
    def put(self, request):
        serializer = StatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                status_obj = update_status(serializer.validated_data)
                response_serializer = StatusResponseSerializer(status_obj)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except StatusNotFound as e:
                return Response({"detail": str(e.detail)}, status=e.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Status"])
class StatusDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Eliminar estado",
        parameters=[OpenApiParameter("id", str, required=True)],
        responses={200: StatusResponseSerializer},
    )
    def delete(self, request):
        try:
            status_obj = delete_status(request.query_params.get("id"))
            serializer = StatusResponseSerializer(status_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except StatusNotFound as e:
            return Response({"detail": str(e.detail)}, status=e.status_code)
