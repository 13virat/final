from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import ProductCategory,Maker,Products

from products.serializers import MakerSerializer, ProductCategorySerializer, ProductsSerializer
class ProductCategoryListView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class= ProductCategorySerializer
class MakerListView(ListAPIView):
    queryset = Maker.objects.all()
    serializer_class= MakerSerializer 
class ProductsListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class= ProductsSerializer               
    