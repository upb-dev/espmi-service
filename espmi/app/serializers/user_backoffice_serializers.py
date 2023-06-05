from espmi.app.models import UserBackOffice
from rest_framework import serializers


class UserBackOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBackOffice
        fields = "__all__"
