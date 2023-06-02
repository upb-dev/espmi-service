
from espmi.app.models import UnitPenunjang
from espmi.app.serializers.unit_penunjang_serializers import UnitPenunjangSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class UnitPenunjangViewSet(BaseModelViewSet):
    queryset = UnitPenunjang.objects.all()
    serializer_class = UnitPenunjangSerializer
