from espmi.app.models import Indikator
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class IndikatorSerializer(BaseModelSerializer):
    class Meta:
        model = Indikator
        fields = "__all__"
