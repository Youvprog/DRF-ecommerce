from unicodedata import category
from django.shortcuts import render

from .serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product


class LatestProductList(APIView):
    def get(self, request, format=None):
        latest_products = Product.objects.all()[0:4]
        s = ProductSerializer(latest_products, many=True)
        return Response(s.data)


@api_view(['GET'])
def get_single_product(request,slug):
    product = Product.objects.get(slug=slug)
    s = ProductSerializer(product, many=False)
    return Response(s.data)

@api_view(['GET'])
def get_category_products(request, cat_slug):
    products_by_cat = Product.objects.filter(category__slug=cat_slug)
    s = ProductSerializer(products_by_cat, many=True)
    return Response(s.data)

@api_view(['GET'])
def get_all_products(request):
    all_products = Product.objects.all()
    s = ProductSerializer(all_products, many=True)
    return Response(s.data)

class AlltProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    


#@api_view(['GET'])
#def get_products(request):#
#    products = Product.objects.all()[0:4]
#    s = ProductSerializer(products, many=True)
#    return Response(s.data)

