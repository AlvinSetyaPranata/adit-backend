from rest_framework import serializers
from .models import Religion, Gender, Citizen

class ReligionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=100)
    # code = serializers.CharField(max_length=10)
    
    # def create(self, validated_data):
    #     return super().create(validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.save()
    #     return instance
    
    class Meta:
        model = Religion
        fields = '__all__'

class ReligionListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields ='__all__'

class GenderListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)

class CitizenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = '__all__'

class CitizenListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=10)