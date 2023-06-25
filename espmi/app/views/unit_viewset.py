
from espmi.app.models import Unit
from espmi.app.serializers.unit_serializers import UnitSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class UnitViewSet(BaseModelViewSet):
    queryset = Unit.objects.all().order_by("created_at")
    serializer_class = UnitSerializer
