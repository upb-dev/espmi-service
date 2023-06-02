from espmi.app.models import Standar
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class StandarSerializer(BaseModelSerializer):
    class Meta:
        model = Standar
        fields = "__all__"
