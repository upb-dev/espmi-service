
from espmi.app.models import EvaluasiDiri
from espmi.app.serializers.evaluasi_diri_serializers import EvaluasiDiriSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class EvaluasiDiriViewSet(BaseModelViewSet):
    queryset = EvaluasiDiri.objects.all().order_by('created_at')
    serializer_class = EvaluasiDiriSerializer
