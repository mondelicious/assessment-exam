from django_filters.rest_framework import FilterSet
from django_filters import CharFilter

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cars.api.serializers import CarsSerializer, ColorsSerializer

from cars.models import Cars as cars, Colors as colors


class CarsFilter(FilterSet):
    color = CharFilter(field_name='color__name', lookup_expr='icontains')

    class Meta:
        model = cars
        fields = ('color',)


class CarsViewSet(viewsets.ModelViewSet):
    queryset = cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [IsAuthenticated]
    filter_class = (CarsFilter)


class ColorsViewSet(viewsets.ModelViewSet):
    queryset = colors.objects.all()
    serializer_class = ColorsSerializer
    permission_classes = [IsAuthenticated]