
from espmi.app.models import SpmiGroup
from espmi.app.serializers.spmi_group_serializers import SpmiGroupSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class SpmiGroupViewSet(BaseModelViewSet):
    queryset = SpmiGroup.objects.all()
    serializer_class = SpmiGroupSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        return super().list(request, *args, **kwargs)
