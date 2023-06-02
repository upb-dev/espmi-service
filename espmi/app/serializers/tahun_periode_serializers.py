from espmi.app.models import TahunPeriode
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class TahunPeriodeSerializer(BaseModelSerializer):
    class Meta:
        model = TahunPeriode
        fields = "__all__"
