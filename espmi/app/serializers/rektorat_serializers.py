from espmi.app.models import Rektorat
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class RektoratSerializer(BaseModelSerializer):
    class Meta:
        model = Rektorat
        fields = "__all__"
