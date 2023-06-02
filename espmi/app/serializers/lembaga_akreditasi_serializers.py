from espmi.app.models import LembagaAkreditasi
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class LembagaAkreditasiSerializer(BaseModelSerializer):
    class Meta:
        model = LembagaAkreditasi
        fields = "__all__"
