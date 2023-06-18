
from espmi.app.filters.nilai_mutu_filter import NilaiMutuFilter
from espmi.app.models import NilaiMutu
from espmi.app.serializers.nilai_mutu_serializers import NilaiMutuSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class NilaiMutuViewSet(BaseModelViewSet):
    queryset = NilaiMutu.objects.all()
    serializer_class = NilaiMutuSerializer
    filterset_class = NilaiMutuFilter
    search_fields = ['desc', 'nilai_mutu']
