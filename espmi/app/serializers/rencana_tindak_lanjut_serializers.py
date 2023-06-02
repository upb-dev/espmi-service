from espmi.app.models import RencanaTindakLanjut
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class RencanaTindakLanjutSerializer(BaseModelSerializer):
    class Meta:
        model = RencanaTindakLanjut
        fields = "__all__"
