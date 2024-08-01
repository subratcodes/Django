from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


class ProductView(APIView):

    parser_classes = [JSONParser]


    def get(self,request,*args,**kwargs):

        print(type(request.data))
        return Response({'received data': request.data})
    


    
        
