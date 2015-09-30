from storeApi.models import Product
from storeApi.serializers import ProductSerializer
from rest_framework import generics
from rest_framework import permissions

class ProductList(generics.ListCreateAPIView):
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        queryset = Product.objects.all()
        serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        queryset = Product.objects.all()
        serializer_class = ProductSerializer 
