from django.urls import path, include
from rest_framework import routers

from .views import InvoiceViews

router = routers.DefaultRouter()
router.register(r'add-invoice', InvoiceViews)
urlpatterns = [
    path('', include(router.urls)),

]