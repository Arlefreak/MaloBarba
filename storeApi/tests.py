from django.test import TestCase
from storeApi.models import *
from storeApi.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class TestProduct(TestCase):
        def test_Create(self):
                p = Product(name="oil", description="Oil 4 u")
                p.save()
                p = Product(name="oil", description="Balm 4 U")
                p.save()
                p = Product(name="Balm", description="Balm 4 U")
                p.save()
        def test_Get(self):
                p = Product(name="oil", description="Oil 4 u")
                p.save()
                p = Product(name="oil", description="Balm 4 U")
                p.save()
                p = Product(name="Balm", description="Balm 4 U")
                p.save()
                oil  = Product.objects.filter(name = "oil")
                balm = Product.objects.filter(name = "balm")
        def test_Serializer(self):
                p = Product(name="oil", description="Oil 4 u")
                p.save()
                x = Product(name="oil", description="Balm 4 U")
                x.save()
                i = Product(name="Balm", description="Balm 4 U")
                i.save()
                serializer = ProductSerializer(Product.objects.all(), many=True)
                print(serializer.data)

class TestProductImages(TestCase):
        def test_Create(self):
                p = Product(name="oil", description="Oil 4 u")
                p.save()
                pi = ProductImages(product=p,name="image")
                pi.save()
        def test_Get(self):
                p = Product(name="oil", description="Oil 4 u")
                p.save()
                pi = ProductImages(product=p,name="image")
                pi.save()
                image = ProductImages.objects.filter(name="image")
        def test_Serializer(self):
                p = Product(name="oil", description="Oil 4 u")
                p.save()
                pi = ProductImages(product=p,name="image")
                pi.save()
                serializer = ProductImageSerializer(ProductImages.objects.all(), many=True)
                print("\n______________________\n")
                print(serializer.data)
