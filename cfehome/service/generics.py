from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


