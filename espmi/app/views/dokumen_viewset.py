from espmi.app.filters.dokumen_filter import DokumenFilter
from espmi.app.models import Dokumen
from espmi.app.serializers.dokumen_serializers import DokumenSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class DokumenViewSet(BaseModelViewSet):
    queryset = Dokumen.objects.all()
    serializer_class = DokumenSerializer
    filterset_class = DokumenFilter
