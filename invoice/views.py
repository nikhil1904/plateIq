from django.http import Http404
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import InvoiceSerializer, InvoiceSummarySerializer
from .models import Invoice, InvoiceSummary
# Create your views here.


class InvoiceViews(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    lookup_field = 'id'

