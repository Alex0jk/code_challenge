from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import IngredientSerializer, SizeSerializer,OrderSerializer, ClientSerializer,OrderGetSerializer
from .models import Ingredient,Size,Order,Client
import json
# Create your views here.
class Ingr():
    def __init__(self,_item,_count):
        self.item=_item
        self.count=_count

class IngredientView(APIView):
    def get(self, request):
        queryset = Ingredient.objects.all()
        serializer = IngredientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(request, format=None):
        serializer = IngredientSerializer(data=request.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "ingredient created succesfully"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class SizeView(APIView):
    def get(self, request):
        queryset = Size.objects.all()
        serializer = SizeSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(request, format=None):
        serializer = SizeSerializer(data=request.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "size created succesfully"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class OrderView(APIView):
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderGetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(request, format=None):
        serializer = OrderSerializer(data=request.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "size created succesfully"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

class OrderDetailView(APIView):
    def get(self, request, order_id):
        queryset = Order.objects.get(id_order=order_id)
        serializer = OrderGetSerializer(queryset)
        return Response(serializer.data)

class MostPopularIngredientView(APIView):
    def get(self,request):
        queryset = Order.objects.all()
        items = OrderGetSerializer(queryset,many=True)
        ingredients_dict={}
        data_list=[]
        print(items.data[0]['details_order']['ingredients'])
        for order in items.data:
            for ingredient in order['details_order']['ingredients']:
                ingredients_dict.setdefault(ingredient,0)
                ingredients_dict[ingredient]+=1
        for k, v in ingredients_dict.items():
            data_list.append(Ingr(k,v))
        data_list=sorted(data_list,key=lambda x:x.count, reverse=True)
        
        return Response([x.__dict__ for x in data_list])

class ClientView(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(request, format=None):
        serializer = ClientSerializer(data=request.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "size created succesfully"})
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)