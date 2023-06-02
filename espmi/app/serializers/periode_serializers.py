from espmi.app.models import Periode
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class PeriodeSerializer(BaseModelSerializer):
    class Meta:
        model = Periode
        fields = "__all__"
