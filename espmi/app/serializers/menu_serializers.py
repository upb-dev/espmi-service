from espmi.app.models import Menu
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class MenuSerializer(BaseModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
