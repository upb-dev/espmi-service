from espmi.app.models import LembagaAkreditasi, ProgramStudi, TahunPeriode, TargetNilaiMutu
from rest_framework import serializers

from espmi.app.serializers.lembaga_akreditasi_serializers import LembagaAkreditasiSerializer
from espmi.app.serializers.program_studi_serializers import ProgramStudiSerializer
from espmi.app.serializers.tahun_periode_serializers import TahunPeriodeSerializer


class TargetNilaiMutuSerializer(serializers.ModelSerializer):
    program_studi = serializers.PrimaryKeyRelatedField(write_only=True, queryset=ProgramStudi.objects.all())
    tahun = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TahunPeriode.objects.all())
    lembaga_akreditasi = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LembagaAkreditasi.objects.all())
    program_studi_data = ProgramStudiSerializer(read_only=True, source='program_studi')

    class Meta:
        model = TargetNilaiMutu
        fields = "__all__"


class TargetNilaiMutuDetailSerializer(serializers.ModelSerializer):
    lembaga_akreditasi_data = LembagaAkreditasiSerializer(read_only=True, source='lembaga_akreditasi')
    tahun_data = TahunPeriodeSerializer(read_only=True, source='tahun')
    program_studi_data = ProgramStudiSerializer(read_only=True, source='program_studi')

    class Meta:
        model = TargetNilaiMutu
        fields = "__all__"
