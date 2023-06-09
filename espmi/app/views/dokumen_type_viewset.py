
from espmi.app.models import DocumentType
from espmi.app.serializers.dokumen_type_serializers import DokumenTypeSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class DokumentTypeViewSet(BaseModelViewSet):
    queryset = DocumentType.objects.all().order_by('created_at')
    serializer_class = DokumenTypeSerializer
