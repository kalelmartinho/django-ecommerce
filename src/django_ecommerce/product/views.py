from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema


from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    ViewSet for viewing and editing categories.
    """

    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request: Request, *args, **kwargs) -> Response:
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    ViewSet for viewing and editing brands.
    """

    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request: Request, *args, **kwargs) -> Response:
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ViewSet):
    """
    ViewSet for viewing and editing products.
    """

    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request: Request, *args, **kwargs) -> Response:
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
