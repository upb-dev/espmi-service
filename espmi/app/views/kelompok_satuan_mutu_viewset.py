
from espmi.app.models import KelompokSatuanMutu
from espmi.app.serializers.kelompok_satuan_mutu_serializers import KelompokSatuanMutuSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class KelompokSatuanMutuViewSet(BaseModelViewSet):
    queryset = KelompokSatuanMutu.objects.all()
    serializer_class = KelompokSatuanMutuSerializer
