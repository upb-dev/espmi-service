
from espmi.app.models import Menu
from espmi.app.serializers.menu_serializers import MenuSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class MenuViewSet(BaseModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
