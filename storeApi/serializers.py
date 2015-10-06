from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from storeApi.models import *

class ProductSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Product
        fields = ('pk','sku','name','image','description','price','discount','inventory','status','tags','category','date','updated','order',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk','name','image','date','updated','order',)

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('product', 'name', 'image', 'order', 'date', 'updated',)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('user',)

class ShoppingCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartProduct
        fields = ('client', 'product', 'cuantity')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('sku','client', 'shippingAdress', 'billingAdress', 'items_subTotal', 'shipping_cost', 'total', 'shipping_carrier', 'shipping_tracking', 'date', 'updated', 'status',)

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = ('client', 'name', 'type', 'default', 'firstname', 'lastname', 'adress_line1', 'adress_line2', 'city', 'state_province', 'country', 'zipcode', 'phone_number', 'date',)
