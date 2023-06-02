from espmi.app.models import SubMenu
from espmi.app.serializers.base_model_serializers import BaseModelSerializer


class SubMenuSerializer(BaseModelSerializer):
    class Meta:
        model = SubMenu
        fields = "__all__"
