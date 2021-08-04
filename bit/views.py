from django.shortcuts import render

# Create your views here.
from rest_framework import routers, serializers, viewsets, status
from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Bitcoin
from .serializer import BitcoinSerializer
from django.http import HttpResponse
import json

class BitcoinViewSet(viewsets.ModelViewSet):

    queryset = Bitcoin.objects.all()
    serializer_class = BitcoinSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return HttpResponse(json.dumps({"price": serializer.data['price']}, ensure_ascii=False), content_type="application/json")

    def get_queryset(self):
        queryset = Bitcoin.objects.all()
        return queryset


