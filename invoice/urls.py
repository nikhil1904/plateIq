from django.urls import path, include
from rest_framework import routers

from .views import InvoiceViews, InvoiceSummaryViews

router = routers.DefaultRouter()
router.register(r'add-invoice', InvoiceViews, 'invoice-list')
router.register(r'invoice-summary', InvoiceSummaryViews, 'invoice-summary-list')
urlpatterns = [
    path('', include(router.urls)),

]