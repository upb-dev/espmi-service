from espmi.app.models import SatuanMutu
from espmi.app.serializers.satuan_mutu_serializers import SatuanMutuSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class SatuanMutuViewSet(BaseModelViewSet):
    queryset = SatuanMutu.objects.all()
    serializer_class = SatuanMutuSerializer
