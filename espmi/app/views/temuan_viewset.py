
from espmi.app.filters.temuan_filter import TemuanFilter
from espmi.app.models import Temuan
from espmi.app.serializers.temuan_serializers import TemuanSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class TemuanViewSet(BaseModelViewSet):
    queryset = Temuan.objects.all().order_by("created_at")
    serializer_class = TemuanSerializer
    filterset_class = TemuanFilter
