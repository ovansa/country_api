from rest_framework import generics
from country.models import Country, State, City
from country.serializers import CountrySerializer, StateSerializer, \
                                CitySerializer
from django_filters.rest_framework import DjangoFilterBackend
from country.filters import StateListFilter

# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status


# ---------------------------------------------------
# Based on generic APIView
# ---------------------------------------------------

class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED,
    # headers=headers)
    #     return Response(serializer.errors,
    # status=status.HTTP_400_BAD_REQUEST)


class CountryDetail(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['country__name',]
    filter_class = StateListFilter


class StateDetail(generics.RetrieveUpdateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# Based on Viewsets

# class CountryViewSet(viewsets.ModelViewSet):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#
# class StateViewSet(viewsets.ModelViewSet):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer
#     filter_backends = [DjangoFilterBackend, ]
#     filter_class = StateListFilter
#
#     def perform_create(self, serializer):
#         serializer.save()
#
#
#
# class CityViewSet(viewsets.ModelViewSet):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer
#
#     def perform_create(self, serializer):
#         serializer.save()
