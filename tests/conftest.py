from pytest_factoryboy import register
from rest_framework.test import APIClient
from tests.factories import BrandFactory, CategoryFactory, ProductFactory
import pytest

register(BrandFactory)
register(CategoryFactory)
register(ProductFactory)

pytest.fixture


def client():
    return APIClient()
