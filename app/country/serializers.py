from rest_framework import serializers
from country.models import Country, State, City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'name', 'state']

class StateSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)
    country = serializers.ReadOnlyField(source='country.name')
    # Check and add source

    class Meta:
        model = State
        fields = ['id', 'name', 'capital', 'country', 'cities']


class CountrySerializer(serializers.ModelSerializer):
    # states = serializers.StringRelatedField(many=True)
    states = StateSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'capital', 'alpha2code', 'alpha3code', 'region', 'states']
