from espmi.app.models import Visitasi
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class VisitasiSerializer(BaseModelSerializer):
    class Meta:
        model = Visitasi
        fields = "__all__"
