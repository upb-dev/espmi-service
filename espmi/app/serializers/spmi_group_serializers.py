from espmi.app.models import SpmiGroup
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class SpmiGroupSerializer(BaseModelSerializer):
    class Meta:
        model = SpmiGroup
        fields = "__all__"
