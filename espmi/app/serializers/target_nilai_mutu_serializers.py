from espmi.app.models import TargetNilaiMutu
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class TargetNilaiMutuSerializer(BaseModelSerializer):
    class Meta:
        model = TargetNilaiMutu
        fields = "__all__"
