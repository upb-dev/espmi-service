
from espmi.app.models import Fakultas
from espmi.app.serializers.fakultas_serializers import FakultasSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class FakultasViewSet(BaseModelViewSet):
    queryset = Fakultas.objects.all()
    serializer_class = FakultasSerializer
