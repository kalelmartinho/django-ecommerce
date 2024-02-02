import factory


from django_ecommerce.product.models import Brand, Product


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker('company')
