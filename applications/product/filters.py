import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name')
    brand = django_filters.CharFilter(field_name='brand__name')

    class Meta:
        model = Product
        fields = ['category', 'brand']