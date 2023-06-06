from espmi.app.models import Auditor, LembagaAkreditasi, ProgramStudi, Unit
from rest_framework import serializers
from espmi.app.serializers.lembaga_akreditasi_serializers import LembagaAkreditasiSerializer

from espmi.app.serializers.unit_serializers import UnitSerializer


class AuditorSerializer(serializers.ModelSerializer):
    lembaga_akreditasi = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LembagaAkreditasi.objects.all())
    jenis_kelamin = serializers.CharField(read_only=True, source='get_gender_display')
    units = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Unit.objects.all())
    units_data = UnitSerializer(many=True, read_only=True, source='units_id')
    lembaga_akreditasi_data = LembagaAkreditasiSerializer(read_only=True, source="lembaga_akreditasi")

    class Meta:
        model = Auditor
        fields = "__all__"
