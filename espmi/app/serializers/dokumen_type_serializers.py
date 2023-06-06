from espmi.app.models import DocumentCategory, DocumentType
from rest_framework import serializers

from espmi.app.serializers.dokumen_category_serializers import DokumenCategorySerializer


class DokumenTypeSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(write_only=True, queryset=DocumentCategory.objects.all())
    category_data = DokumenCategorySerializer(read_only=True, source="category")

    class Meta:
        model = DocumentType
        fields = "__all__"
