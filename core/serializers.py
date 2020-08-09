from rest_framework import serializers
from .models import Client, Company

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number'
        )


#company serializer
class CompanySerializer(serializers.Serializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
        )