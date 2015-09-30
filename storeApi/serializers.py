from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from storeApi.models import *

class ProductSerializer(TaggitSerializer,serializers.ModelSerializer):
        tags = TagListSerializerField()
        class Meta:
            model = Product
            fields = ('pk','sku','name','image','description','price','discount','inventory','status','tags','date','updated','order',)

