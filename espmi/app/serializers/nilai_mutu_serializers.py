from espmi.app.models import LembagaAkreditasi, NilaiMutu, TahunPeriode
from rest_framework import serializers


class NilaiMutuSerializer(serializers.ModelSerializer):
    tahun = serializers.PrimaryKeyRelatedField(write_only=True, queryset=TahunPeriode.objects.all())
    lembaga_akreditasi = serializers.PrimaryKeyRelatedField(write_only=True, queryset=LembagaAkreditasi.objects.all())

    class Meta:
        model = NilaiMutu
        fields = "__all__"
