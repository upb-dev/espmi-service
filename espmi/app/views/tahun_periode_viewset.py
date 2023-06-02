
from espmi.app.models import TahunPeriode
from espmi.app.serializers.tahun_periode_serializers import TahunPeriodeSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class TahunPeriodeViewSet(BaseModelViewSet):
    queryset = TahunPeriode.objects.all()
    serializer_class = TahunPeriodeSerializer
