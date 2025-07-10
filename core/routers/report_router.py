from django.urls import path
from core.views.report_view import ReportCreateView, ReportListView

urlpatterns = [
    path("reports/list/", ReportListView.as_view(), name="report-list"),
    path('reports/create/', ReportCreateView.as_view(), name='report-create'),
]
