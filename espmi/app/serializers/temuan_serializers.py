from espmi.app.models import Temuan
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class TemuanSerializer(BaseModelSerializer):
    class Meta:
        model = Temuan
        fields = "__all__"
