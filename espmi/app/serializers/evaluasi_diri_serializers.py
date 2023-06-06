from espmi.app.models import Dokumen, EvaluasiDiri, Indikator, SubStandar
from espmi.app.serializers.base_model_serializers import BaseModelSerializer
from rest_framework import serializers
from espmi.app.serializers.dokumen_serializers import DokumenSerializer
from espmi.app.serializers.indikator_serializers import IndikatorSerializer

from espmi.app.serializers.sub_standar_serializers import SubStandarSerializer


class EvaluasiDiriSerializer(BaseModelSerializer):
    sub_standar = serializers.PrimaryKeyRelatedField(write_only=True, queryset=SubStandar.objects.all())
    indikator = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Indikator.objects.all())
    dokumen = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Dokumen.objects.all())
    sub_standar_data = SubStandarSerializer(read_only=True, source='sub_standar')
    indikator_data = IndikatorSerializer(read_only=True, source='indikator')
    dokumen_data = DokumenSerializer(read_only=True, many=True, source='dokumen')

    class Meta:
        model = EvaluasiDiri
        fields = "__all__"
