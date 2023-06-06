from espmi.app.models import Indikator, SubStandar, Visitasi
from espmi.app.serializers.base_model_serializers import BaseModelSerializer
from rest_framework import serializers
from espmi.app.serializers.indikator_serializers import IndikatorSerializer

from espmi.app.serializers.sub_standar_serializers import SubStandarSerializer


class VisitasiSerializer(BaseModelSerializer):
    sub_standar = serializers.PrimaryKeyRelatedField(write_only=True, queryset=SubStandar.objects.all())
    indikator = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Indikator.objects.all())
    sub_standar_data = SubStandarSerializer(read_only=True, source='sub_standar')
    indikator_data = IndikatorSerializer(read_only=True, source='indikator')

    class Meta:
        model = Visitasi
        fields = "__all__"
