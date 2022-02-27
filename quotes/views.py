from django.shortcuts import render

# Create your views here.
from quotes.models import Quotes
from quotes.serializers import QuotesSerializer
from rest_framework import viewsets


class QuotesViewSet(viewsets.ModelViewSet):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer
