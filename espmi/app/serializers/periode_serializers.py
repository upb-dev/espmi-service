from espmi.app.models import Periode
from rest_framework import serializers


class PeriodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periode
        fields = "__all__"
