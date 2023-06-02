
from espmi.app.models import UserPortal
from espmi.app.serializers.user_portal_serializers import UserPortalSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class UserPortalViewSet(BaseModelViewSet):
    queryset = UserPortal.objects.all()
    serializer_class = UserPortalSerializer
