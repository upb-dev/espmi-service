from espmi.app.models import ProgramStudi
from rest_framework import serializers


class ProgramStudiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramStudi
        fields = "__all__"
