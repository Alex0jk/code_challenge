from rest_framework import serializers
from .models import Order,Client,Ingredient,Size

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields=('name_ingredient','price_ingredient')

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields=('name_size','price_size')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields=('id_client','name_client')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields=('id_client','details_order','price_order')

class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        depth=2
        fields=('id_order','id_client','details_order','price_order')