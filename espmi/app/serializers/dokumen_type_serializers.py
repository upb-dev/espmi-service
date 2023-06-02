from espmi.app.models import DocumentType
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class DokumenTypeSerializer(BaseModelSerializer):
    class Meta:
        model = DocumentType
        fields = "__all__"
