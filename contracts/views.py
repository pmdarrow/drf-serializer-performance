from rest_framework import viewsets, mixins
from .models import Person
from .serializers import PortfolioSerializer, PersonSerializer


class PortfolioViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = PortfolioSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
