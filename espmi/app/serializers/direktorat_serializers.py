from espmi.app.models import Direktorat
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class DirektoratSerializer(BaseModelSerializer):
    class Meta:
        model = Direktorat
        fields = "__all__"
