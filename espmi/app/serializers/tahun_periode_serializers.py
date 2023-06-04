from espmi.app.models import TahunPeriode
from rest_framework import serializers


class TahunPeriodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TahunPeriode
        fields = "__all__"
