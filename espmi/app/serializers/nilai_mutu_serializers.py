from espmi.app.models import NilaiMutu
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class NilaiMutuSerializer(BaseModelSerializer):
    class Meta:
        model = NilaiMutu
        fields = "__all__"
