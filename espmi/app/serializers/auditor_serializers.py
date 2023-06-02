from espmi.app.models import Auditor
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class AuditorSerializer(BaseModelSerializer):
    class Meta:
        model = Auditor
        fields = "__all__"
