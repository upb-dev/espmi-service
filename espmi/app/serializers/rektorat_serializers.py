from espmi.app.models import Rektorat
from rest_framework import serializers


class RektoratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rektorat
        fields = "__all__"
