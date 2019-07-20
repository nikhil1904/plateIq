from rest_framework import serializers
from .models import Invoice, InvoiceSummary, InvoiceState


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceSummary
        fields = "__all__"


class InvoiceStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceState
        fields = "__all__"
