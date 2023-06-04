from espmi.app.models import UnitPenunjang
from rest_framework import serializers


class UnitPenunjangSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitPenunjang
        fields = "__all__"
