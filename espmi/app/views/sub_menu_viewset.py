
from espmi.app.models import SubMenu
from espmi.app.serializers.sub_menu_serializers import SubMenuSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class SubMenuViewSet(BaseModelViewSet):
    queryset = SubMenu.objects.all().order_by("created_at")
    serializer_class = SubMenuSerializer
