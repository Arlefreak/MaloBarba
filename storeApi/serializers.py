from rest_framework                import serializers
from django.contrib.auth.models    import User
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from storeApi.models               import *
from taggit.models                 import Tag

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
    def create(self, validated_data):
        client_data = validated_data.pop('client', None)
        user = super(ClientSerializer, self).create(validated_data)
        self.create_or_update_client(user, client_data)
        return user
    def update(self, instance, validated_data):
        client_data = validated_data.pop('client', None)
        self.create_or_update_client(instance, client_data)
        return super(UserSerializer, self).update(instance, validated_data)
    def create_or_update_profile(self, user, client_data):
        client, created = Client.objects.get_or_create(user=user, defaults=client_data)
        if not created and client_data is not None:
            super(ClientSerializer, self).update(client, client_data)

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

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

