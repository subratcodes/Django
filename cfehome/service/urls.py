from django.urls import path
from .views import *
from .viewV2 import ProductView
from .mixins import ProductList,SingleProduct
from .generics import ProductList

urlpatterns=[
     path('products/all',ProductList.as_view()),
     path('products/<int:pk>',SingleProduct.as_view()),
   #  path("products/create",MyOwnView.as_view()),
#     path("products/retrive/<pk>",RetrieveProductView.as_view()),
#     path("products/update/<pk>",UpdateAPIView.as_view()),
#     path("products/delete/<pk>",DestoryProductView.as_view()),
   # path("products/custom",MyOwnView.as_view())
   path("products/v2",ProductView.as_view())
 ]  