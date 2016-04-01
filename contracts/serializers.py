from rest_framework import serializers
from .models import Contract, Portfolio, CURRENCY_CHOICES


class MoneySerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.ChoiceField(choices=CURRENCY_CHOICES)
    value_date = serializers.DateTimeField(required=False, allow_null=True)
    rate = serializers.FloatField(required=False, allow_null=True, min_value=0)
    rate_currency = serializers.ChoiceField(choices=CURRENCY_CHOICES,
                                            required=False, allow_blank=True)


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    premium = MoneySerializer()
    limit = MoneySerializer()
    franchise = MoneySerializer()
    attachment = MoneySerializer()

    class Meta:
        model = Contract
        fields = ('name', 'date', 'premium', 'limit', 'franchise', 'attachment')

    def create(self, validated_data):
        return Contract.objects.create(**validated_data)


class PortfolioSerializer(serializers.Serializer):
    contracts = ContractSerializer(many=True)

    class Meta:
        model = Portfolio

    def create(self, validated_data):
        return validated_data
