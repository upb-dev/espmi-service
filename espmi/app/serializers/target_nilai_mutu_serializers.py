from espmi.app.models import TargetNilaiMutu
from rest_framework import serializers


class TargetNilaiMutuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetNilaiMutu
        fields = "__all__"
