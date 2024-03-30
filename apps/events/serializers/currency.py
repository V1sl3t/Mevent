from rest_framework import serializers

from apps.events.models import Currency


class CurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "name"]
