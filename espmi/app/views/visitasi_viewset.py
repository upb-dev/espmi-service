
from espmi.app.models import Visitasi
from espmi.app.serializers.visitasi_serializers import VisitasiSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class VisitasiViewSet(BaseModelViewSet):
    queryset = Visitasi.objects.all().order_by("created_at")
    serializer_class = VisitasiSerializer
