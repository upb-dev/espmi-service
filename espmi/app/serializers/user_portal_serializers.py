from espmi.app.models import UserPortal
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class UserPortalSerializer(BaseModelSerializer):
    class Meta:
        model = UserPortal
        fields = "__all__"
