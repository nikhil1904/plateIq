from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import InvoiceViews, InvoiceSummaryViews, UpdateInvoiceStateView, GetInvoiceSummary, GetInvoiceState

router = routers.DefaultRouter()
router.register(r'add-invoice', InvoiceViews, 'invoice-list')
router.register(r'invoice-summary', InvoiceSummaryViews, 'invoice-summary-list')
urlpatterns = [
    path('', include(router.urls)),
    path('digitized-state-update/', UpdateInvoiceStateView.as_view()),
    path('get-invoice-summary/', GetInvoiceSummary.as_view()),
    path('get-invoice-state/', GetInvoiceState.as_view()),

]
