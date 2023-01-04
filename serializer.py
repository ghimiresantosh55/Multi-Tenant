'''
Serializer for tenant
'''
from rest_framework import serializers
from .models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    '''
    Serializer class for tenant
    '''
    class Meta:
        model = Tenant
        fields = "__all__"
