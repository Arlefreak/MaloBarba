from storeApi.models           import *
from storeApi.serializers      import *
from rest_framework            import permissions
from rest_framework            import viewsets

class ProductViewSet(viewsets.ModelViewSet):
        queryset           = Product.objects.all()
        serializer_class   = ProductSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProductImagesViewset(viewsets.ModelViewSet):
        queryset           = ProductImages.objects.all()
        serializer_class   = ProductImageSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
