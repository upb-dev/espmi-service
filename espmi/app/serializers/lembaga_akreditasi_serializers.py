from espmi.app.models import LembagaAkreditasi
from rest_framework import serializers


class LembagaAkreditasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LembagaAkreditasi
        fields = ["id", "name", "desc"]
