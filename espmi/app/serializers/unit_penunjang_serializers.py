from espmi.app.models import UnitPenunjang
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class UnitPenunjangSerializer(BaseModelSerializer):
    class Meta:
        model = UnitPenunjang
        fields = "__all__"
