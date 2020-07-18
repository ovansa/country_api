from django.db import models
import uuid


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    capital = models.CharField(max_length=100)
    alpha2code = models.CharField(max_length=100, unique=True)
    alpha3code = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class State(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    capital = models.CharField(max_length=100, default='None')
    country = models.ForeignKey(Country, related_name='states',
                                on_delete=models.CASCADE)
    # country = models.ManyToManyField('Country')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey(State, related_name='cities',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
