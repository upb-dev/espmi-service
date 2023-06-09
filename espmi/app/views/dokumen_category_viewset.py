
from espmi.app.models import DocumentCategory
from espmi.app.serializers.dokumen_category_serializers import DokumenCategorySerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class DokumenCategoryViewSet(BaseModelViewSet):
    queryset = DocumentCategory.objects.all().order_by('created_at')
    serializer_class = DokumenCategorySerializer
