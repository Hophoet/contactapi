from django.shortcuts import render
from django.http import JsonResponse

#
#from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

#
from .models import Client, Company
#
from .serializers import ClientSerializer, CompanySerializer



class TestView(APIView):
    
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
    
        serializer = ClientSerializer(clients, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pass
        # serializer = PostSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)

