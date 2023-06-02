from espmi.app.models import Fakultas
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class FakultasSerializer(BaseModelSerializer):
    class Meta:
        model = Fakultas
        fields = "__all__"
