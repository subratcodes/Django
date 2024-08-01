from django.urls import path,include
from .views import *
from .viewV2 import ProductView
from .mixins import ProductList,SingleProduct
from .generics import ProductList
from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSets

router=DefaultRouter()
router.register('students',ProductViewSets)

urlpatterns=[
       path('',include(router.urls)),
#      path('products/all',ProductList.as_view()),
#      path('products/<int:pk>',SingleProduct.as_view()),
#    #  path("products/create",MyOwnView.as_view()),
# #     path("products/retrive/<pk>",RetrieveProductView.as_view()),
# #     path("products/update/<pk>",UpdateAPIView.as_view()),
# #     path("products/delete/<pk>",DestoryProductView.as_view()),
#    # path("products/custom",MyOwnView.as_view())
#    path("products/v2",ProductView.as_view())
 ]  



