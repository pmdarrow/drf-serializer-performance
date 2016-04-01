from rest_framework import serializers
from .models import Contract, Portfolio, Person, CURRENCY_CHOICES


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


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    authors = PersonRelatedField(
        many=True,
        queryset=Person.objects.all(),
        view_name='person-detail',
    )
    premium = MoneySerializer()
    limit = MoneySerializer()
    franchise = MoneySerializer()
    attachment = MoneySerializer()

    class Meta:
        model = Contract
        fields = (
            'name',
            'type',
            'date',
            'authors',
            'premium',
            'limit',
            'franchise',
            'attachment',
        )

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)


class PortfolioSerializer(serializers.Serializer):
    contracts = ContractSerializer(many=True)

    class Meta:
        model = Portfolio

    def create(self, validated_data):
        return validated_data

    def to_internal_value(self, data):
        global person_cache
        person_cache = {p.pk: p for p in Person.objects.all()}
        return super().to_internal_value(data)
