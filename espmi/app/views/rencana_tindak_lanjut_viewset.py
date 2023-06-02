
from espmi.app.filters.rencana_tindak_lanjut_filter import RencanaTindakLanjutFilter
from espmi.app.models import RencanaTindakLanjut
from espmi.app.serializers.rencana_tindak_lanjut_serializers import RencanaTindakLanjutSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class RencanaTindakLanjutViewSet(BaseModelViewSet):
    queryset = RencanaTindakLanjut.objects.all()
    serializer_class = RencanaTindakLanjutSerializer
    filterset_class = RencanaTindakLanjutFilter
