from espmi.app.models import LembagaAkreditasi, ProgramStudi, TahunPeriode, TargetNilaiMutu
from rest_framework import serializers


class TargetNilaiMutuSerializer(serializers.ModelSerializer):
    program_studi = serializers.PrimaryKeyRelatedField(write_only=True, queryset=ProgramStudi.objects.all())
    tahun = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TahunPeriode.objects.all())
    lembaga_akreditasi = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LembagaAkreditasi.objects.all())

    class Meta:
        model = TargetNilaiMutu
        fields = "__all__"
