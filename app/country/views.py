# from rest_framework import generics
from country.models import Country, State, City
from country.serializers import CountrySerializer, StateSerializer, \
                                CitySerializer
from django_filters.rest_framework import DjangoFilterBackend
from country.filters import StateListFilter

from rest_framework import viewsets


# ---------------------------------------------------
# Based on generic APIView
# ---------------------------------------------------

# class CountryList(generics.ListCreateAPIView):
#     queryset = Country.objects.all().order_by('name')
#     serializer_class = CountrySerializer
#
#
# class CountryDetail(generics.RetrieveUpdateAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer

# class StateList(generics.ListCreateAPIView):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer
#     filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['country__name',]
#     filter_class = StateListFilter
#
#
# class CityList(generics.ListCreateAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def perform_create(self, serializer):
        serializer.save()


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_class = StateListFilter

    def perform_create(self, serializer):
        serializer.save()


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def perform_create(self, serializer):
        serializer.save()
