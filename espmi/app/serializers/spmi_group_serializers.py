from espmi.app.models import SpmiGroup
from rest_framework import serializers


class SpmiGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpmiGroup
        fields = "__all__"
