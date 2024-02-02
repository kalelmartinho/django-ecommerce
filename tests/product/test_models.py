import pytest

pytestmark = pytest.mark.django_db 

class TestBrandModel:
    def test_str_method(self, brand_factory):
        brand = brand_factory()
        assert str(brand) == brand.name 

class TestCategoryModel:
    def test_str_method(self, category_factory):
        category = category_factory()
        assert str(category) == category.name

class TestProductModel:
    def test_str_method(self, product_factory):
        product = product_factory()
        assert str(product) == product.name
