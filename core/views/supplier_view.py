from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_spectacular.utils import extend_schema

from core.serializers.supplier_serializer import (
    SupplierCreateSerializer,
    SupplierResponseSerializer,
    SupplierUpdateSerializer,
)
from core.services.supplier_service import (
    create_supplier,
    list_suppliers,
    update_supplier,
    delete_supplier,
)
from core.exceptions.supplier_exceptions import (
    SupplierAlreadyExists,
    SupplierNotFound,
)

@extend_schema(tags=["Suppliers"])
class SupplierCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=SupplierCreateSerializer, responses={201: SupplierResponseSerializer})
    def post(self, request):
        serializer = SupplierCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                supplier = create_supplier(serializer.validated_data)
                return Response(SupplierResponseSerializer(supplier).data, status=status.HTTP_201_CREATED)
            except SupplierAlreadyExists as e:
                return Response({"detail": str(e)}, status=e.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(tags=["Suppliers"])
class SupplierListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(responses=SupplierResponseSerializer(many=True))
    def get(self, request):
        suppliers = list_suppliers()
        return Response(SupplierResponseSerializer(suppliers, many=True).data)

@extend_schema(tags=["Suppliers"])
class SupplierUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(request=SupplierUpdateSerializer, responses={200: SupplierResponseSerializer})
    def put(self, request):
        serializer = SupplierUpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                supplier = update_supplier(serializer.validated_data)
                return Response(SupplierResponseSerializer(supplier).data)
            except SupplierNotFound as e:
                return Response({"detail": str(e)}, status=e.status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(tags=["Suppliers"])
class SupplierDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(responses={204: None})
    def delete(self, request, id):
        try:
            delete_supplier(id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SupplierNotFound as e:
            return Response({"detail": str(e)}, status=e.status_code)