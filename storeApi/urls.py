from .                      import views
from django.conf.urls       import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'productsImages', views.ProductImagesViewset)
router.register(r'client', views.ClientViewset)
router.register(r'shoppingCartProduct', views.ShoppingCartProductViewset)
router.register(r'order', views.OrderViewSet)
router.register(r'adress', views.AdressViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
