from espmi.app.models import KelompokSatuanMutu, LembagaAkreditasi, SatuanMutu, TahunPeriode, Unit
from espmi.app.serializers.base_model_serializers import BaseModelSerializer
from rest_framework import serializers
from espmi.app.serializers.kelompok_satuan_mutu_serializers import KelompokSatuanMutuSerializer

from espmi.app.serializers.lembaga_akreditasi_serializers import LembagaAkreditasiSerializer
from espmi.app.serializers.tahun_periode_serializers import TahunPeriodeSerializer
from espmi.app.serializers.unit_serializers import UnitSerializer


class SatuanMutuSerializer(BaseModelSerializer):
    lembaga_akreditasi = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LembagaAkreditasi.objects.all())
    jenjang = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Unit.objects.all())
    tahun = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TahunPeriode.objects.all())
    lembaga_akreditasi_data = LembagaAkreditasiSerializer(read_only=True, source='lembaga_akreditasi')
    jenjang_data = UnitSerializer(read_only=True, many=True, source='jenjang')
    tahun_data = TahunPeriodeSerializer(read_only=True, source="tahun")
    kelompok_satuan_mutu = serializers.PrimaryKeyRelatedField(write_only=True, queryset=KelompokSatuanMutu.objects.all())
    kelompo_satuan_mutu_data = KelompokSatuanMutuSerializer(read_only=True, source='kelompok_satuan_mutu')

    class Meta:
        model = SatuanMutu
        fields = "__all__"
