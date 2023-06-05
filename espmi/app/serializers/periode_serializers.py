from espmi.app.models import LembagaAkreditasi, Periode, StandarNasional, TahunPeriode
from rest_framework import serializers
from espmi.app.serializers.lembaga_akreditasi_serializers import LembagaAkreditasiSerializer
from espmi.app.serializers.standar_nasional_serializers import StandarNasionalSerializer

from espmi.app.serializers.tahun_periode_serializers import TahunPeriodeSerializer


class PeriodeSerializer(serializers.ModelSerializer):
    tahun_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TahunPeriode.objects.all())
    lembaga_akreditasi_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LembagaAkreditasi.objects.all())
    standar_nasional_id = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=StandarNasional.objects.all())
    tahun = TahunPeriodeSerializer(read_only=True, source='tahun_id')
    lembaga_akreditasi = LembagaAkreditasiSerializer(read_only=True, source='lembaga_akreditasi_id')
    standar_nasional = StandarNasionalSerializer(read_only=True, many=True, source='standar_nasional_id')

    class Meta:
        model = Periode
        fields = "__all__"
