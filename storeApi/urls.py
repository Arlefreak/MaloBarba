from .                      import views
from django.conf.urls       import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'productImage', views.ProductImagesViewset)
router.register(r'category', views.CategoryViewset)
router.register(r'user', views.UserViewset)
router.register(r'shoppingCartProduct', views.ShoppingCartProductViewset)
router.register(r'order', views.OrderViewSet)
router.register(r'adress', views.AdressViewSet)
router.register(r'tag', views.TaggitViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
