from django.http import Http404

from .models import Invoice, InvoiceSummary, InvoiceState


def get_invoice_obj(invoice_id):
    try:
        return Invoice.objects.get(id=invoice_id)
    except Invoice.DoesNotExist:
        raise Http404


def get_invoice_summary_obj_by_invoice(invoice_id):
    try:
        return InvoiceSummary.objects.get(invoice__id=invoice_id)
    except InvoiceSummary.DoesNotExist:
        return None

def get_invoice_state_obj_by_invoice(invoice_id):
    try:
        return InvoiceState.objects.get(invoice__id=invoice_id)
    except InvoiceState.DoesNotExist:
        raise Http404