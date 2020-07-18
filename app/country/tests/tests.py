from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from country.models import Country  # State, City
from country.serializers import CountrySerializer


COUNTRY_URL = reverse('country:country-list')


class APITests(TestCase):
    '''Test the available apis'''

    def setUp(self):
        self.client = APIClient()

    def test_get_list_of_countries(self):
        '''Test returning the list of countries'''
        Country.objects.create(name='Nigeria', capital='Abuja',
                               alpha2code='NG',
                               alpha3code='NGA', region='Africa')
        Country.objects.create(name='Ghana', capital='Accra', alpha2code='GH',
                               alpha3code='GHA', region='Africa')

        client = APIClient()
        res = client.get(COUNTRY_URL)

        countries = Country.objects.all()

        serializer = CountrySerializer(countries, many=True)

        print(res.data)
        print('\n')
        print(serializer.data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_country(self):
        '''Test creating a new country successfully'''
        payload = {
            'name': 'Ghana',
            'capital': 'Accra',
            'alpha2code': 'GH',
            'alpha3code': 'GHA',
            'region': 'Africa'
        }

        res = self.client.post(COUNTRY_URL, payload)

        exists = Country.objects.filter(
            name=payload['name']
        ).exists

        self.assertTrue(exists)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_existing_country(self):
        '''Test creating country using duplicate name'''

        payload1 = {
            'name': 'Ghana',
            'capital': 'Accra',
            'alpha2code': 'GH',
            'alpha3code': 'GHA',
            'region': 'Africa'
        }

        payload2 = {
            'name': 'Ghana',
            'capital': 'Abuja',
            'alpha2code': 'NG',
            'alpha3code': 'NGA',
            'region': 'Africa'
        }

        self.client.post(COUNTRY_URL, payload1)
        res2 = self.client.post(COUNTRY_URL, payload2)

        self.assertEqual(res2.status_code, status.HTTP_400_BAD_REQUEST)
