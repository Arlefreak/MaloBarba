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

class CategoryViewset(viewsets.ModelViewSet):
        queryset           = Category.objects.all()
        serializer_class   = CategorySerializer 
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ClientViewset(viewsets.ModelViewSet):
        queryset           = Client.objects.all()
        serializer_class   = ClientSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ShoppingCartProductViewset(viewsets.ModelViewSet):
        queryset           = ShoppingCartProduct.objects.all()
        serializer_class   = ShoppingCartProductSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class OrderViewSet(viewsets.ModelViewSet):
        queryset           = Order.objects.all()
        serializer_class   = OrderSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AdressViewSet(viewsets.ModelViewSet):
        queryset           = Adress.objects.all()
        serializer_class   = AdressSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
