from espmi.app.models import NilaiMutu
from rest_framework import serializers


class NilaiMutuSerializer(serializers.ModelSerializer):
    class Meta:
        model = NilaiMutu
        fields = "__all__"
