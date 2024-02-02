from rest_framework.test import APIClient
import pytest

pytestmark = pytest.mark.django_db


class TestBrandRouter:
    endpoint = "/api/brand/"

    def test_list_brand(self, brand_factory, client):
        brand_factory.create_batch(3)
        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.json()) == 3


class TestCategoryRouter:
    endpoint = "/api/category/"

    def test_list_category(self, category_factory, client):
        category_factory.create_batch(3)
        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.json()) == 3


class TestProductRouter:
    endpoint = "/api/product/"
    
    def test_list_product(self, product_factory, client):
        product_factory.create_batch(3)
        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.json()) == 3
