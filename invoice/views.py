from django.shortcuts import render
from rest_framework import status, viewsets
from .serializers import InvoiceSerializer, InvoiceSummarySerializer
from .models import Invoice, InvoiceSummary, User
# Create your views here.


class InvoiceViews(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        return Invoice.objects.filter(created_by=self.request.user)
    model = Invoice
    lookup_field = 'id'


class InvoiceSummaryViews(viewsets.ModelViewSet):
    serializer_class = InvoiceSummarySerializer
    queryset = InvoiceSummary.objects.all()


