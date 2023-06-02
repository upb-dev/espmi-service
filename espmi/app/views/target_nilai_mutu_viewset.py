
from espmi.app.models import TargetNilaiMutu
from espmi.app.serializers.target_nilai_mutu_serializers import TargetNilaiMutuSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class TargetNilaiMutuViewSet(BaseModelViewSet):
    queryset = TargetNilaiMutu.objects.all()
    serializer_class = TargetNilaiMutuSerializer
