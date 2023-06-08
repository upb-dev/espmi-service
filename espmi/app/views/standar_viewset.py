
from espmi.app.models import Standar
from espmi.app.serializers.standar_serializers import StandarSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class StandarViewSet(BaseModelViewSet):
    queryset = Standar.objects.all().order_by("created_at")
    serializer_class = StandarSerializer
