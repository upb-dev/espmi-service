from espmi.app.models import UserPortal
from rest_framework import serializers


class UserPortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPortal
        fields = "__all__"
