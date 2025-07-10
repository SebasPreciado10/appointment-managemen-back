from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_spectacular.utils import extend_schema, OpenApiParameter

from core.serializers.product_subline_serializer import (
    ProductSublineCreateSerializer,
    ProductSublineResponseSerializer,
    ProductSublineUpdateSerializer,
)
from core.services.product_subline_service import (
    create_product_subline,
    list_product_sublines,
    update_product_subline,
    delete_product_subline,
)
from core.exceptions.product_subline_exceptions import (
    ProductSublineAlreadyExists,
    ProductSublineNotFound,
)


@extend_schema(tags=["Product Sublines"])
class ProductSublineCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Crear una sublínea de producto",
        request=ProductSublineCreateSerializer,
        responses={201: ProductSublineResponseSerializer},
    )
    def post(self, request):
        serializer = ProductSublineCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                subline = create_product_subline(serializer.validated_data)
                response_serializer = ProductSublineResponseSerializer(subline)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            except ProductSublineAlreadyExists as e:
                return Response({"detail": str(e.detail)}, status=e.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Product Sublines"])
class ProductSublineListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Listar sublíneas de producto",
        responses={200: ProductSublineResponseSerializer(many=True)},
    )
    def get(self, request):
        sublines = list_product_sublines()
        serializer = ProductSublineResponseSerializer(sublines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=["Product Sublines"])
class ProductSublineUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Actualizar sublínea de producto",
        request=ProductSublineUpdateSerializer,
        responses={200: ProductSublineResponseSerializer},
    )
    def put(self, request):
        serializer = ProductSublineUpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                subline = update_product_subline(serializer.validated_data)
                response_serializer = ProductSublineResponseSerializer(subline)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except ProductSublineNotFound as e:
                return Response({"detail": str(e.detail)}, status=e.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["Product Sublines"])
class ProductSublineDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Eliminar sublínea de producto",
        parameters=[OpenApiParameter("id", str, required=True)],
        responses={200: ProductSublineResponseSerializer},
    )
    def delete(self, request):
        try:
            subline = delete_product_subline(request.query_params.get("id"))
            serializer = ProductSublineResponseSerializer(subline)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProductSublineNotFound as e:
            return Response({"detail": str(e.detail)}, status=e.status_code)