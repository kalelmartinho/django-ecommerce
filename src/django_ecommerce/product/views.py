from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from drf_spectacular.utils import extend_schema


from .models import Brand, Category
from .serializers import BrandSerializer, CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    ViewSet for viewing and editing categories.
    """

    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializer)
    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    ViewSet for viewing and editing brands.
    """

    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)
