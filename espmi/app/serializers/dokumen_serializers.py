from espmi.app.models import DocumentType, Dokumen
from espmi.app.serializers import dokumen_type_serializers
from espmi.app.serializers.base_model_serializers import BaseModelSerializer
from rest_framework import serializers


class DokumenSerializer(BaseModelSerializer):
    type_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=DocumentType.objects.all())
    type = dokumen_type_serializers.DokumenTypeSerializer(read_only=True, source="type_id")

    class Meta:
        model = Dokumen
        fields = "__all__"
