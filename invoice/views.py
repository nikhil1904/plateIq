from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .obj_helper import get_invoice_obj, get_invoice_summary_obj_by_invoice, get_invoice_state_obj_by_invoice
from django.db.models.signals import post_save
from django.dispatch import receiver
from .serializers import InvoiceSerializer, InvoiceSummarySerializer, InvoiceStateSerializer
from .models import Invoice, InvoiceSummary, InvoiceState
from .constants import INVOICE_NOT_DIGITIZED


class InvoiceViews(viewsets.ModelViewSet):
    """
    Viewset to upload, update and list invoices
    :class:`core.models.`Invoice` .

    **Permission** : Super Admin, Network Admin
    """
    # permission_classes = (IsAuthenticated, )
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    # We can show only invoices which were created by that user only by below queryset

    # def get_queryset(self):
    #     return Invoice.objects.filter(created_by=self.request.user)
    model = Invoice
    lookup_field = 'id'


class InvoiceSummaryViews(viewsets.ModelViewSet):
    """
    Viewset to post, list, update Invoice summary.
    :class:`core.models.`InvoiceSummary` .

    **Permission** : Super Admin, Internal User
    """
    serializer_class = InvoiceSummarySerializer
    queryset = InvoiceSummary.objects.all()


class UpdateInvoiceStateView(APIView):
    """
        Functionality of updating state of invoice from pending to Digitized or declined
        :class:`core.models.InvoiceState

        **Permission:** Super Admin, Internal User

        :put:
        Update the status of given invoice.
    """

    def put(self, request):
        """

        :param request:
        :return: Invoice state
        """
        invoice_id = request.data.get("id")
        state = int(request.data.get("state"))
        invoice_summary_obj = get_invoice_summary_obj_by_invoice(invoice_id)
        if not invoice_summary_obj:
            return Response({"success": False, "message": INVOICE_NOT_DIGITIZED})
        invoice_state_obj = InvoiceState.objects.get(invoice__id=invoice_id)
        serializer = InvoiceStateSerializer(invoice_state_obj, data={"state": state})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetInvoiceSummary(APIView):
    """
        Functionality of getting Invoice.Summary for digitized invoice
        :class:`core.models.InvoiceSummary

        **Permission:** Super Admin, Network Admin, AgencyAdmin, AdvertiserAdmin, OperatorAdmin

        :get:
        Get invoice summary of given digitized invoice
    """

    def get(self, request):
        """

        :param request:
        :return: Invoice Summary
        """
        invoice_id = request.GET.get("id")
        invoice_summary_obj = get_invoice_summary_obj_by_invoice(invoice_id)
        if not invoice_summary_obj:
            return Response({"succes":False, "message": INVOICE_NOT_DIGITIZED})
        return Response(InvoiceSummarySerializer(invoice_summary_obj).data)


class GetInvoiceState(APIView):
    """
        Functionality of getting state of given invoice
        :class:`core.models.`InvoiceState`

        **Permission:** Super Admin, Customer

        :get:
        Get state of given invoice.
    """
    def get(self, request):
        """

        :param request:
        :return: Invoice State of given invoice
        """
        invoice_id = request.GET.get("id")
        invoice_state_obj = get_invoice_state_obj_by_invoice(invoice_id)
        return Response(InvoiceStateSerializer(invoice_state_obj).data)


@receiver(post_save, sender=Invoice)
def create_invoice_state(sender, instance, created, **kwargs):
    """
    signal function used to create Invoice state(default=pending) whenever user creates, update the invoice
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        InvoiceState.objects.create(invoice=instance, state=InvoiceState.Pending)
