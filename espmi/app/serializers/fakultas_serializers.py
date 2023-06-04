from espmi.app.models import Fakultas
from rest_framework import serializers


class FakultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultas
        fields = "__all__"
