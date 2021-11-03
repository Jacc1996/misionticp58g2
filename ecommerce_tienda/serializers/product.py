from django.db.models import fields
from rest_framework import serializers
from ecommerce_tienda.models import Product

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'