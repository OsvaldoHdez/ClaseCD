from os import CLD_CONTINUED, stat
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets
import rest_framework
from rest_framework.response import Response
from .serializers import ClientSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics

import requests
from .models import Client
# Create your views here.

class Index(generic.TemplateView):
    template_name = "home/index.html"

    def get(self, request):
        numbers = [i for i in range(10)]
        queryset = User.objects.all()
        context = {
            'message': "Hola mundo desde CS",
            'numbers': numbers,
            'users': queryset
        }
        return render(request, "home/index.html", context)

class ListClientView(generic.ListView):
    template_name = "home/list_client.html"
    model = Client
    # queryset = Client.objects.all()  -----> select * from Client

class PokeView(generic.TemplateView):
    template_name = "home/pokelist.html"

    def get (self, request):
        url = "https://pokeapi.co/api/v2/pokemon/gengar"
        response = requests.get(url)
        r = response.json()
        context = {
            "pokemon": r["moves"]
        }
        return render(request, "home/pokelist.html", context)
    
def wsClient(request):
    queryset = Client.objects.all()
    data = serializers.serialize('json', queryset)
    return HttpResponse(data, content_type="application/json")

class ViewWsClient(generic.TemplateView):
    template_name = "home/view_ws_client.html"
    
    def get(self, request):
        url = "http://localhost:8000/home/ws/clients/"
        response = requests.get(url)
        context = {
            "obj": response.json()
        }
        return render(request, "home/view_ws_client.html", context)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

@api_view(["GET", "POST"])
def client_list(request):
    if request.method=="GET":
        clients = Client.objects.all()
        data = ClientSerializer(clients, many = True)
        return Response(data.data, status=status.HTTP_200_OK)
    elif request.method=="POST":
        data = ClientSerializer(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def client_update(request, pk=None):
    client = Client.objects.filter(id=pk).first()
    if client:
        if request.method=="GET":
            data = ClientSerializer(client)
            return Response(data.data, status=status.HTTP_200_OK)
        elif request.method=="PUT":
                data = ClientSerializer(client, data = request.data)
                if data.is_valid():
                    data.save()
                    return Response(data.data, status=status.HTTP_200_OK)
                return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method=="DELETE":
            return Response()
    return Response({"message": "Client Not Found"}, status=status.HTTP_400_BAD_REQUEST)

class ClientListAPIView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        data = ClientSerializer(clients, many=True)
        return Response(data.data,status=status.HTTP_200_OK)

class DetailClientAPIView(APIView):
    def get(self, request, pk):
        client = Client.objects.filter(id=pk).first()
        data = ClientSerializer(client)
        return Response(data.data, status=status.HTTP_200_OK)

class ClientListCreate(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = ClientSerializer.Meta.model.objects.filter(status=True)#Client.objects.filter(status=True)

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    queryset = ClientSerializer.Meta.model.objects.all()

