from espmi.app.models import Direktorat
from rest_framework import serializers


class DirektoratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direktorat
        fields = "__all__"
