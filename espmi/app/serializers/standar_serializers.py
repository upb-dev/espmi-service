from espmi.app.models import LembagaAkreditasi, SatuanMutu, Standar, TahunPeriode, Unit
from espmi.app.serializers.base_model_serializers import BaseModelSerializer
from rest_framework import serializers

from espmi.app.serializers.lembaga_akreditasi_serializers import LembagaAkreditasiSerializer
from espmi.app.serializers.satuan_mutu_serializers import SatuanMutuSerializer
from espmi.app.serializers.tahun_periode_serializers import TahunPeriodeSerializer
from espmi.app.serializers.unit_serializers import UnitSerializer


class StandarSerializer(BaseModelSerializer):
    lembaga_akreditasi = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LembagaAkreditasi.objects.all())
    jenjang = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Unit.objects.all())
    tahun = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TahunPeriode.objects.all())
    lembaga_akreditasi_data = LembagaAkreditasiSerializer(read_only=True, source='lembaga_akreditasi')
    jenjang_data = UnitSerializer(read_only=True, many=True, source='jenjang')
    tahun_data = TahunPeriodeSerializer(read_only=True, source="tahun")
    satuan_mutu = serializers.PrimaryKeyRelatedField(write_only=True, queryset=SatuanMutu.objects.all())
    satuan_mutu_data = SatuanMutuSerializer(read_only=True, source='satuan_mutu')

    class Meta:
        model = Standar
        fields = "__all__"
