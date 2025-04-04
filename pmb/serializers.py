from rest_framework import serializers
from .models import *

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class ParentListSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50, allow_blank=True, required=False)
    nik = serializers.CharField(max_length=16)
    kk = serializers.CharField(max_length=16)
    address = serializers.CharField()
    contact = serializers.CharField(max_length=15)
    job = serializers.CharField(source='job.__str__', read_only=True)
    income = serializers.CharField(source='income.__str__', read_only=True)

    class Meta:
        model = Parent
        fields = [
            'id', 'first_name', 'last_name', 'nik', 'kk', 
            'address', 'contact', 'job', 'income'
        ]