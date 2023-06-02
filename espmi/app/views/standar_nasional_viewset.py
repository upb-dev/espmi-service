
from espmi.app.models import StandarNasional
from espmi.app.serializers.standar_nasional_serializers import StandarNasionalSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class StandarNasionalViewSet(BaseModelViewSet):
    queryset = StandarNasional.objects.all()
    serializer_class = StandarNasionalSerializer
