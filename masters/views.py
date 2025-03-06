from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Religion
from .serializers import ReligionSerializer
# Create your views here.

class ReligionList(APIView):
    def get(self, request, format=None):
        religions = Religion.objects.all()
        serializer = ReligionSerializer(religions, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ReligionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReligionDetail(APIView):
    def get_object(self, pk):
        try:
            return Religion.objects.get(pk=pk)
        except Religion.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        religion = self.get_object(pk)
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)
    
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