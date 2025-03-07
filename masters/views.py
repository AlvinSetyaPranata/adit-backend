from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Religion
from .serializers import ReligionSerializer, ReligionListSerializer

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