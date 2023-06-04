from espmi.app.models import Indikator
from rest_framework import serializers


class IndikatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indikator
        fields = "__all__"
