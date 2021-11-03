from django.shortcuts import render
from rest_framework import viewsets
from ecommerce_tienda.serializers.product import ProductoSerializer
from ecommerce_tienda.models import Product

# Create your views here.
class ProductosViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Product.objects.all()