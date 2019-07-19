from rest_framework import serializers
from .models import Invoice, InvoiceSummary


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceSummary
        fields = "__all__"
