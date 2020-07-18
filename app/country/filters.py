import django_filters
from country.models import State

class StateListFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name='country__name', lookup_expr='icontains')

    class Meta:
        model = State
        fields = ['country',]
