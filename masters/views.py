from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Religion, Gender, Citizen, Province
from .serializers import ReligionSerializer, ReligionListSerializer, GenderSerializer, GenderListSerializer, CitizenSerializer, CitizenListSerializer, ProvinceSerializer, ProvinceListSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

# ini class untuk metode GET dan POST
class ReligionList(APIView):
    
    @swagger_auto_schema(
        query_serializer=ReligionListSerializer,
        responses={200: ReligionSerializer(many=True)},
        tags=['Religion'],
    )
        
    def get(self, request, format=None):
        religions = Religion.objects.all()
        serializer = ReligionSerializer(religions, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name','code'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['Religion'],
    )
    def post(self, request, format=None):
        serializer = ReligionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ini class untuk metode GET, PUT, dan DELETE
class ReligionDetail(APIView):
    def get_object(self, pk):
        try:
            return Religion.objects.get(pk=pk)
        except Religion.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=ReligionSerializer,
        responses={200: ReligionSerializer},
        tags=['Religion'],
    )
    def get(self, request, pk, format=None):
        religion = self.get_object(pk)
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=ReligionSerializer,
        request_body=ReligionSerializer,
        responses={200: ReligionSerializer},
        tags=['Religion']
    )
    def put(self, request, pk, format=None):
        religion = self.get_object(pk)
        serializer = ReligionSerializer(religion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        religion = self.get_object(pk)
        religion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenderList(APIView):

    @swagger_auto_schema(
        query_serializer=GenderListSerializer,
        responses={200: GenderSerializer(many=True)},
        tags=['Gender'],
    )
        
    def get(self, request, format=None):
        genders = Gender.objects.all()
        serializer = GenderSerializer(genders, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name','code'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['Gender'],
    )
    def post(self, request, format=None):
        serializer = GenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenderDetail(APIView):
    def get_object(self, pk):
        try:
            return Gender.objects.get(pk=pk)
        except Gender.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=GenderSerializer,
        responses={200: GenderSerializer},
        tags=['Gender'],
    )
    def get(self, request, pk, format=None):
        gender = self.get_object(pk)
        serializer = GenderSerializer(gender)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=GenderSerializer,
        request_body=GenderSerializer,
        responses={200: GenderSerializer},
        tags=['Gender']
    )
    def put(self, request, pk, format=None):
        gender = self.get_object(pk)
        serializer = GenderSerializer(gender, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        gender = self.get_object(pk)
        gender.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serialzer = CitizenSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CitizenList(APIView):

    @swagger_auto_schema(
        query_serializer=CitizenListSerializer,
        responses={200: CitizenSerializer(many=True)},
        tags=['Citizen'],
    )
        
    def get(self, request, format=None):
        citizens = Citizen.objects.all()
        serializer = CitizenSerializer(citizens, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name','code'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        security=[],
        tags=['Citizen'],
    )
    def post(self, request, format=None):
        serializer = CitizenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CitizenDetail(APIView):
    def get_object(self, pk):
        try:
            return Citizen.objects.get(pk=pk)
        except Citizen.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=CitizenSerializer,
        responses={200: CitizenSerializer},
        tags=['Citizen'],
    )
    def get(self, request, pk, format=None):
        citizen = self.get_object(pk)
        serializer = CitizenSerializer(citizen)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=CitizenSerializer,
        request_body=CitizenSerializer,
        responses={200: CitizenSerializer},
        tags=['Citizen']
    )
    def put(self, request, pk, format=None):
        citizen = self.get_object(pk)
        serializer = CitizenSerializer(citizen, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        citizen = self.get_object(pk)
        citizen.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProvinceList(APIView):

    @swagger_auto_schema(
        query_serializer=ProvinceListSerializer,
        responses={200: ProvinceSerializer(many=True)},
        tags=['Province'],
    )
    def get(self, request, format=None):
        provinces = Province.objects.all()
        serializer = ProvinceSerializer(provinces, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Create a new province",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'code', 'meta'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'code': openapi.Schema(type=openapi.TYPE_STRING),
                'meta': openapi.Schema(type=openapi.TYPE_OBJECT)
            },
        ),
        security=[],
        tags=['Province'],
    )
    def post(self, request, format=None):
        serializer = ProvinceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProvinceDetail(APIView):
    def get_object(self, pk):
        try:
            return Province.objects.get(pk=pk)
        except Province.DoesNotExist:
            raise Http404
    
    @swagger_auto_schema(
        query_serializer=ProvinceSerializer,
        responses={200: ProvinceSerializer},
        tags=['Province'],
    )
    def get(self, request, pk, format=None):
        province = self.get_object(pk)
        serializer = ProvinceSerializer(province)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        query_serializer=ProvinceSerializer,
        request_body=ProvinceSerializer,
        responses={200: ProvinceSerializer},
        tags=['Province']
    )
    def put(self, request, pk, format=None):
        province = self.get_object(pk)
        serializer = ProvinceSerializer(province, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        province = self.get_object(pk)
        province.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
