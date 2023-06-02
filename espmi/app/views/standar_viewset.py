
from espmi.app.models import Standar
from espmi.app.serializers.standar_serializers import StandarSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class StandarViewSet(BaseModelViewSet):
    queryset = Standar.objects.all()
    serializer_class = StandarSerializer
