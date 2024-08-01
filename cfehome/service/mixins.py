

from rest_framework import generics,mixins
from .models import Product
from .serializers import ProductSerializer

class ProductList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    """
    Mixins work with the database 

    But generrcis works with the request responses and API controles.
    """
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)




class SingleProduct(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer


    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)