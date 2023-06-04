from espmi.app.models import DocumentType
from rest_framework import serializers


class DokumenTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = "__all__"
