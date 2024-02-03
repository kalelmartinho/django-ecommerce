import factory


from django_ecommerce.product.models import Brand, Category, Product


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:  # type: ignore
        model = Brand

    name = factory.Faker("company")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:  # type: ignore
        model = Category

    name = factory.Faker("word")
    description = factory.Faker("sentence")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:  # type: ignore
        model = Product

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    is_active = factory.Faker("boolean")
