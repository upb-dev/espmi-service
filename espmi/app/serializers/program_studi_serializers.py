from espmi.app.models import Fakultas, ProgramStudi
from rest_framework import serializers

from espmi.app.serializers.fakultas_serializers import FakultasSerializer


class ProgramStudiSerializer(serializers.ModelSerializer):
    fakultas_rel = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Fakultas.objects.all())
    fakultas = FakultasSerializer(read_only=True, source='fakultas_rel')
    akreditasi_type = serializers.IntegerField(write_only=True)
    akreditasi = serializers.CharField(read_only=True, source='get_akreditasi_type_display')

    class Meta:
        model = ProgramStudi
        fields = "__all__"
