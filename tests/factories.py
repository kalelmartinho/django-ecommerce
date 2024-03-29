import factory


from django_ecommerce.product.models import Brand, Category, Product


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker("company")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")
    description = factory.Faker("sentence")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
