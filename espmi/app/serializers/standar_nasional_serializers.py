from espmi.app.models import StandarNasional
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class StandarNasionalSerializer(BaseModelSerializer):
    class Meta:
        model = StandarNasional
        fields = "__all__"
