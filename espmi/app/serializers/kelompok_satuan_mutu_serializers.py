from espmi.app.models import KelompokSatuanMutu
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class KelompokSatuanMutuSerializer(BaseModelSerializer):
    class Meta:
        model = KelompokSatuanMutu
        fields = "__all__"
