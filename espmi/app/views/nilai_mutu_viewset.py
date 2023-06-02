
from espmi.app.models import NilaiMutu
from espmi.app.serializers.nilai_mutu_serializers import NilaiMutuSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class NilaiMutuViewSet(BaseModelViewSet):
    queryset = NilaiMutu.objects.all()
    serializer_class = NilaiMutuSerializer
