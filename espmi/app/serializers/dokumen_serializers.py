from espmi.app.models import Dokumen
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class DokumenSerializer(BaseModelSerializer):
    class Meta:
        model = Dokumen
        fields = "__all__"
