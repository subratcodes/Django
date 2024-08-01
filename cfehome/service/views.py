from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status 


from django.core.serializers import serialize
import json
from rest_framework.generics import (
    ListAPIView,
    GenericAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from .serializers import ProductSerializer

from .models import Product
from rest_framework.views import APIView



class MyOwnView(APIView):


    def get(self,request,*args,**kwargs):
        print(args)

        if request.query_params and request.query_params['id']:
           single_product=self.findProduct(request.query_params['id'])
           
           if single_product is None:return Response(status=status.HTTP_204_NO_CONTENT)
           
           sr_product=ProductSerializer(single_product)
           
           return Response(sr_product.data,status=status.HTTP_200_OK)
        
        # we use serializers so that they can converted into query object to the the JSON structire.
        data=Product.objects.all()[:2]
        serialzed_data=ProductSerializer(data,many=True)
        return Response(serialzed_data.data,status=status.HTTP_200_OK)
        
    

    def findProduct(self,id:int):
       try:
            student=Product.objects.get(pk=id)
        
            return student
       except Product.DoesNotExist:
          return None
       

    
    def post(self,request,*args,**kwargs):
       
       print(type(request.data))
     
       sdata=ProductSerializer(data=request.data)
       
       if sdata.is_valid():
        print("Data is vcalid")
        sdata.save()
        return JsonResponse(sdata.data,status=status.HTTP_201_CREATED)
        
       else: return JsonResponse(sdata.errors,status=status.HTTP_400_BAD_REQUEST)

# class ServiceApiView(ListAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()



class SingluarApiView(APIView):
   def get(self,request, pk):
      try:
         product=Product.objects.get(pk=pk)
         if product is None: return Response(product,status=status.HTTP_404_NOT_FOUND)
         else: return Response(ProductSerializer(product).data,status=status.HTTP_200_OK)
      except Exception:
         print(Exception)
         return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
      
      

class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly]



# class RetrieveProductView(RetrieveAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()



# class UpdateAPIView(UpdateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()



# class DestoryProductView(DestroyAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
      