from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from storeApi.models import *

class ProductSerializer(TaggitSerializer,serializers.ModelSerializer):
        tags = TagListSerializerField(required=False)
        class Meta:
            model = Product
            fields = ('pk','sku','name','image','description','price','discount','inventory','status','tags','date','updated','order',)

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('product', 'name', 'image', 'order', 'date', 'updated')
