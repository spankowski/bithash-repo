from rest_framework import serializers
from .models import Bitcoin

class BitcoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitcoin
        fields = ('amount','price')
        read_only_fields = ('price',)
        write_only_fields = ('amount',)
