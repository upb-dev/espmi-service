
from espmi.app.models import Rektorat
from espmi.app.serializers.rektorat_serializers import RektoratSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class RektoratViewSet(BaseModelViewSet):
    queryset = Rektorat.objects.all()
    serializer_class = RektoratSerializer
