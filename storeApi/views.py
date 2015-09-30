from storeApi.models           import Product
from storeApi.serializers      import ProductSerializer
from rest_framework            import permissions
from rest_framework            import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
