from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .obj_helper import get_invoice_obj, get_invoice_summary_obj_by_invoice, get_invoice_state_obj_by_invoice
from django.db.models.signals import post_save
from django.dispatch import receiver
from .serializers import InvoiceSerializer, InvoiceSummarySerializer, InvoiceStateSerializer
from .models import Invoice, InvoiceSummary, InvoiceState
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


class UpdateInvoiceStateView(APIView):

    def put(self, request):
        invoice_id = request.data.get("id")
        state = int(request.data.get("state"))
        invoice_summary_obj = get_invoice_summary_obj_by_invoice(invoice_id)
        if not invoice_summary_obj:
            return Response({"success": False, "message": "Document is not digitized yet!"})
        invoice_state_obj = InvoiceState.objects.get(invoice__id=invoice_id)
        serializer = InvoiceStateSerializer(invoice_state_obj, data={"state": state})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetInvoiceSummary(APIView):

    def get(self, request):
        invoice_id = request.GET.get("id")
        invoice_summary_obj = get_invoice_summary_obj_by_invoice(invoice_id)
        if not invoice_summary_obj:
            return Response({"succes":False, "message": "Invoice is not digitized yet!"})
        return Response(InvoiceSummarySerializer(invoice_summary_obj).data)


class GetInvoiceState(APIView):
    def get(self, request):
        invoice_id = request.GET.get("id")
        invoice_state_obj = get_invoice_state_obj_by_invoice(invoice_id)
        return Response(InvoiceStateSerializer(invoice_state_obj).data)


@receiver(post_save, sender=Invoice)
def create_invoice_state(sender, instance, created, **kwargs):
    if created:
        InvoiceState.objects.create(invoice=instance, state=InvoiceState.Pending)
