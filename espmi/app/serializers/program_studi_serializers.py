from espmi.app.models import ProgramStudi
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class ProgramStudiSerializer(BaseModelSerializer):
    class Meta:
        model = ProgramStudi
        fields = "__all__"
