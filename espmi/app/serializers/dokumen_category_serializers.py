from espmi.app.models import DocumentCategory
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class DokumenCategorySerializer(BaseModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = "__all__"
