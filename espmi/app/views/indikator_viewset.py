
from espmi.app.models import Indikator
from espmi.app.serializers.indikator_serializers import IndikatorSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class IndikatorViewSet(BaseModelViewSet):
    queryset = Indikator.objects.all()
    serializer_class = IndikatorSerializer
