
from espmi.app.models import LembagaAkreditasi
from espmi.app.serializers.lembaga_akreditasi_serializers import LembagaAkreditasiSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class LembagaAkreditasiViewSet(BaseModelViewSet):
    queryset = LembagaAkreditasi.objects.all().order_by('created_at')
    serializer_class = LembagaAkreditasiSerializer
