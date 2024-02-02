from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for viewing and editing categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
