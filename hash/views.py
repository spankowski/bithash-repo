from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status
from .models import UserHash
from .serializer import UserHashSerializer
from django.http import HttpResponse
import json
from rest_framework import filters, generics

# Create your views here.
# ViewSets define the view behavior.
class UserHashViewSet(viewsets.ModelViewSet):

    queryset = UserHash.objects.all()
    serializer_class = UserHashSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['first_name']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return HttpResponse(json.dumps(serializer.data, ensure_ascii=False), content_type="application/json")

    def get_queryset(self):
        queryset = UserHash.objects.all()
        queryset = queryset.order_by('second_name','first_name')
        return queryset