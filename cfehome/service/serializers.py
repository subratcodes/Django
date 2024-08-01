from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields="__all__"
    


    def validate_price(self,value:int):
        if value<1:raise serializers.ValidationError("Price value cannot be less than 1")
        else: return value
    

    # def validate_price(self, attrs):
    #     if attrs=="-1":raise serializers.ValidationError("Price cannot be less than 0")

        

