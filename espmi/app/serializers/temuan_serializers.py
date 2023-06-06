from espmi.app.models import SubStandar, Temuan
from espmi.app.serializers.base_model_serializers import BaseModelSerializer
from rest_framework import serializers

from espmi.app.serializers.sub_standar_serializers import SubStandarSerializer


class TemuanSerializer(BaseModelSerializer):
    sub_standar = serializers.PrimaryKeyRelatedField(write_only=True, queryset=SubStandar.objects.all())
    sub_standar_data = SubStandarSerializer(read_only=True, source='sub_standar')

    class Meta:
        model = Temuan
        fields = "__all__"
