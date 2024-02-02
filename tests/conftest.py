from pytest_factoryboy import register

from tests.factories import BrandFactory, CategoryFactory, ProductFactory

register(BrandFactory)
register(CategoryFactory)
register(ProductFactory)
