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



class ContactsListView(APIView):
    
    permission_classes = (IsAuthenticated,)

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

class ContactDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        client_id = kwargs.get('client_id')
        client = Client.objects.get(id=client_id)
        company = client.company
        # print(contact, contact.company_set.first())
        client_serializer = ClientSerializer(client)
        company_serializer = CompanySerializer(company)
        return Response(data=(client_serializer.data, company_serializer.data))

class ClientSearchView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')
        if not query:
            #get all the albums if no search
            return Response(status=404)

        else:
            #get the contacts with the query contains
            clients = Client.objects.filter(first_name__icontains=query)
        if not clients.exists():
            #
            clients = Client.objects.filter(last_name__icontains=query)
        if not clients.exists():
             #get all the albums if no search
            return Response(status=404)
        clients = ClientSerializer(clients, many=True)
        return Response(clients.data)
