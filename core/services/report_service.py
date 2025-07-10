# core/services/report_service.py
from core.models.report import Report
from core.models.product_subline import ProductSubline
from django.db import connection


def create_report_for_product_subline(product_subline_id, date_from=None, date_to=None):
    with connection.cursor() as cursor:
        query = """
        SELECT AVG(EXTRACT(EPOCH FROM (actual_delivery - scheduled_delivery)) / 3600) AS average_delivery_time
        FROM appointment
        WHERE product_subline_id = %s
          AND actual_delivery IS NOT NULL
          AND scheduled_delivery IS NOT NULL
          AND actual_delivery >= scheduled_delivery
        """
        
        filters = ""
        params = [product_subline_id]

        if date_from and date_to:
            filters += " AND scheduled_delivery BETWEEN %s AND %s"
            params.extend([date_from, date_to])

        query = query + filters
        
        cursor.execute(query, params)
        result = cursor.fetchone()

    average_delivery_time =  None  
    if result and result[0] != 0 and result[0] is not None:
        average_delivery_time = result[0]
        

    if average_delivery_time is None:
        raise ValueError("No se encontró información sobre el promedio en el rango de fechas proporcionado.")
    
    product_subline = ProductSubline.objects.get(id=product_subline_id)

    report = Report.objects.create(
        product_subline=product_subline,
        average_delivery_time=average_delivery_time
    )

    return report


def list_reports(date_from=None, date_to=None, product_subline_id=None):
    queryset = Report.objects.all()

    if product_subline_id:
        queryset = queryset.filter(product_subline__id=product_subline_id)
    
    if date_from:
        queryset = queryset.filter(generated_at__gte=date_from)
    
    if date_to:
        queryset = queryset.filter(generated_at__lte=date_to)

    reports = queryset.order_by('-generated_at')

    return reports
