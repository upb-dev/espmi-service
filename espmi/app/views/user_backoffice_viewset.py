
from espmi.app.models import UserBackOffice
from espmi.app.serializers.user_backoffice_serializers import UserBackOfficeSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class UserBackOfficeViewSet(BaseModelViewSet):
    queryset = UserBackOffice.objects.all()
    serializer_class = UserBackOfficeSerializer
