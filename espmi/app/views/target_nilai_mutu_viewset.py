
from espmi.app.filters.target_nilai_mutu import TargetNilaiMutuFilter
from espmi.app.models import TargetNilaiMutu
from espmi.app.serializers.target_nilai_mutu_serializers import TargetNilaiMutuSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class TargetNilaiMutuViewSet(BaseModelViewSet):
    queryset = TargetNilaiMutu.objects.all().order_by("created_at")
    serializer_class = TargetNilaiMutuSerializer
    filterset_class = TargetNilaiMutuFilter
    search_fields = ['desc', 'nilai_target']
