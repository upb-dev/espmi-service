from espmi.app.models import LembagaAkreditasi, NilaiMutu, TahunPeriode
from rest_framework import serializers
from espmi.app.serializers.lembaga_akreditasi_serializers import LembagaAkreditasiSerializer

from espmi.app.serializers.tahun_periode_serializers import TahunPeriodeSerializer


class NilaiMutuSerializer(serializers.ModelSerializer):
    tahun = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TahunPeriode.objects.all())
    lembaga_akreditasi = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LembagaAkreditasi.objects.all())
    tahun_data = TahunPeriodeSerializer(read_only=True, source='tahun')
    lembaga_akreditasi_data = LembagaAkreditasiSerializer(read_only=True, source='lembaga_akreditasi')

    class Meta:
        model = NilaiMutu
        fields = "__all__"
