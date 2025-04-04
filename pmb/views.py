from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Parent
from .serializers import ParentSerializer, ParentListSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ParentList(APIView):

    @swagger_auto_schema(
        responses={200: ParentListSerializer(many=True)},
        tags=['Parent'],
    )
    def get(self, request, format=None):
        parents = Parent.objects.all()
        serializer = ParentListSerializer(parents, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ParentSerializer,
        responses={201: ParentSerializer()},
        tags=['Parent'],
    )
    def post(self, request, format=None):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ParentDetail(APIView):
    def get_object(self, pk):
        try:
            return Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: ParentListSerializer()},
        tags=['Parent']
    )
    def get(self, request, pk, format=None):
        parent = self.get_object(pk)
        serializer = ParentListSerializer(parent)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ParentSerializer,
        responses={200: ParentSerializer()},
        tags=['Parent']
    )
    def put(self, request, pk, format=None):
        parent = self.get_object(pk)
        serializer = ParentSerializer(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={204: 'No content'},
        tags=['Parent']
    )
    def delete(self, request, pk, format=None):
        parent = self.get_object(pk)
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)