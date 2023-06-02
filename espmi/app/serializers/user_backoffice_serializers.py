from espmi.app.models import UserBackOffice
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class UserBackOfficeSerializer(BaseModelSerializer):
    class Meta:
        model = UserBackOffice
        fields = "__all__"
