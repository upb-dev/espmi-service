from espmi.app.models import SatuanMutu
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class SatuanMutuSerializer(BaseModelSerializer):
    class Meta:
        model = SatuanMutu
        fields = "__all__"
