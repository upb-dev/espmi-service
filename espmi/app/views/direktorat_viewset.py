
from espmi.app.models import Direktorat
from espmi.app.serializers.direktorat_serializers import DirektoratSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class DirektoratViewSet(BaseModelViewSet):
    queryset = Direktorat.objects.all()
    serializer_class = DirektoratSerializer
