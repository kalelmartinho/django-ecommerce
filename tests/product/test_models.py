import pytest

pytestmark = pytest.mark.django_db 

class TestBrandModel:
    def test_output_str_method(self, brand_factory):
        brand = brand_factory()
        assert str(brand) == brand.name 

class TestCategoryModel:
    pass

class TestProductModel:
    pass
