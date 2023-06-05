from espmi.app.models import Menu
from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    unit_type = serializers.IntegerField(write_only=True)
    unit = serializers.CharField(read_only=True, source='get_unit_type_display')

    class Meta:
        model = Menu
        fields = "__all__"
