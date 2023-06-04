from espmi.app.models import StandarNasional
from rest_framework import serializers


class StandarNasionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandarNasional
        fields = "__all__"
