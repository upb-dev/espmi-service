from espmi.app.models import SubStandar
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class SubStandarSerializer(BaseModelSerializer):
    class Meta:
        model = SubStandar
        fields = "__all__"
