from espmi.app.models import Auditor
from espmi.app.serializers.auditor_serializers import AuditorSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class AuditorViewSet(BaseModelViewSet):
    queryset = Auditor.objects.all().order_by('created_at')
    serializer_class = AuditorSerializer
