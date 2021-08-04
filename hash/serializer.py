from rest_framework import serializers
from .models import UserHash

class UserHashSerializer(serializers.ModelSerializer):
    # dynamic_data = serializers.SerializerMethodField()
    class Meta:
        model = UserHash
        fields = ('first_name','second_name','date_of_birth','hash')
        read_only_fields = ('hash',)
    

