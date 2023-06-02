from espmi.app.models import EvaluasiDiri
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class EvaluasiDiriSerializer(BaseModelSerializer):
    class Meta:
        model = EvaluasiDiri
        fields = "__all__"
