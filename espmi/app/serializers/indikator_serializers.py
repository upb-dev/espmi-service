from espmi.app.models import Indikator, SubStandar
from rest_framework import serializers

from espmi.app.serializers.sub_standar_serializers import SubStandarSerializer


class IndikatorSerializer(serializers.ModelSerializer):
    sub_standar = serializers.PrimaryKeyRelatedField(write_only=True, queryset=SubStandar.objects.all())
    sub_standar_data = SubStandarSerializer(read_only=True, source='sub_standar')

    class Meta:
        model = Indikator
        fields = "__all__"
