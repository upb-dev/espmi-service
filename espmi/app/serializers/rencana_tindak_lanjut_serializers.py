from espmi.app.models import RencanaTindakLanjut, Temuan
from espmi.app.serializers.base_model_serializers import BaseModelSerializer
from rest_framework import serializers

from espmi.app.serializers.temuan_serializers import TemuanSerializer


class RencanaTindakLanjutSerializer(BaseModelSerializer):
    temuan = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Temuan.objects.all())
    temuan_data = TemuanSerializer(read_only=True, source='temuan')

    class Meta:
        model = RencanaTindakLanjut
        fields = "__all__"
