from espmi.app.models import DocumentCategory
from rest_framework import serializers


class DokumenCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = "__all__"
