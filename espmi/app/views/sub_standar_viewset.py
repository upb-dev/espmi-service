
from espmi.app.models import SubStandar
from espmi.app.serializers.sub_standar_serializers import SubStandarSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class SubStandarViewSet(BaseModelViewSet):
    queryset = SubStandar.objects.all()
    serializer_class = SubStandarSerializer
