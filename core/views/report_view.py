# core/views/report_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_spectacular.utils import extend_schema
from core.serializers.report_serializer import ReportCreateSerializer
from core.services.report_service import create_report_for_product_subline, list_reports
from core.models.product_subline import ProductSubline
from core.serializers.report_serializer import ReportResponseSerializer
from drf_spectacular.utils import OpenApiParameter


@extend_schema(
    tags=["Reports"],
    summary="Crear un reporte manualmente",
    description="Genera un reporte de tiempo promedio de entrega para una sublínea de producto específica.",
    request=ReportCreateSerializer,
    responses={201: ReportCreateSerializer},
)
class ReportCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_subline_id = request.data.get('product_subline')
        date_from = request.data.get('date_from')
        date_to = request.data.get('date_to')
        
        if not product_subline_id:
            return Response({"detail": "El campo product_subline es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            report = create_report_for_product_subline(product_subline_id, date_from, date_to)
            serializer = ReportCreateSerializer(report)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ProductSubline.DoesNotExist:
            return Response({"detail": "Sublínea de producto no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
@extend_schema(
    tags=["Reports"],
    summary="Listar reportes de tiempo promedio de entrega",
    parameters=[
        OpenApiParameter("date_from", str, required=False),
        OpenApiParameter("date_to", str, required=False),
        OpenApiParameter("product_subline_id", str, required=False),
    ],
    responses={200: ReportResponseSerializer(many=True)},
)
class ReportListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        product_subline_id = request.query_params.get('product_subline_id')
        
        reports = list_reports(date_from, date_to, product_subline_id)
        
        if not reports:
            return Response({"detail": "No se encontraron reportes para los filtros proporcionados."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReportResponseSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
