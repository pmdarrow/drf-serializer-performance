from rest_framework import serializers
from .models import Person


CONTRACT_TYPES = (
    ('a', 'A'),
    ('b', 'B'),
    ('c', 'C'),
    ('d', 'D'),
    ('e', 'E'),
    ('f', 'F'),
    ('g', 'G'),
    ('h', 'H'),
    ('i', 'I'),
    ('j', 'J'),
)

CURRENCY_CHOICES = (
    ('usd', 'US Dollars'),
    ('cad', 'Canadian Dollars'),
)


class MoneySerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.ChoiceField(choices=CURRENCY_CHOICES)
    value_date = serializers.DateTimeField(required=False, allow_null=True)
    rate = serializers.FloatField(required=False, allow_null=True, min_value=0)
    rate_currency = serializers.ChoiceField(choices=CURRENCY_CHOICES,
                                            required=False, allow_blank=True)


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person


person_cache = None


class PersonRelatedField(serializers.HyperlinkedRelatedField):
    def get_object(self, view_name, view_args, view_kwargs):
        global person_cache
        return person_cache[int(view_kwargs['pk'])]


class SubContractSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    type = serializers.ChoiceField(choices=CONTRACT_TYPES)
    date = serializers.DateTimeField()
    authors = PersonRelatedField(
        many=True,
        queryset=Person.objects.all(),
        view_name='person-detail',
    )
    premium = MoneySerializer()
    limit = MoneySerializer()
    franchise = MoneySerializer()
    attachment = MoneySerializer()


class ContractSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    sub_contracts = SubContractSerializer(many=True)


class PortfolioSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    contracts = ContractSerializer(many=True)

    def create(self, validated_data):
        return validated_data

    def to_internal_value(self, data):
        global person_cache
        person_cache = {p.pk: p for p in Person.objects.all()}
        return super().to_internal_value(data)
