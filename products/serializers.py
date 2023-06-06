from rest_framework import serializers

from products.models import ProductCategory,Maker, Products
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
        depth=1 
class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = "__all__"
class ProductsSerializer(serializers.ModelSerializer):   
     class Meta:
        model = Products
        fields = "__all__"   
        depth=1  