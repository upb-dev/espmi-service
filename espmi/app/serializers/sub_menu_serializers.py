from espmi.app.models import SubMenu
from rest_framework import serializers


class SubMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = "__all__"
