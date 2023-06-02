
from espmi.app.models import Periode
from espmi.app.serializers.periode_serializers import PeriodeSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class PeriodeViewSet(BaseModelViewSet):
    queryset = Periode.objects.all()
    serializer_class = PeriodeSerializer
