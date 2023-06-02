
from espmi.app.filters.program_studi_filter import ProgramStudiFilter
from espmi.app.models import ProgramStudi
from espmi.app.serializers.program_studi_serializers import ProgramStudiSerializer
from espmi.app.views.base_model_viewset import BaseModelViewSet


class ProgramStudiViewSet(BaseModelViewSet):
    queryset = ProgramStudi.objects.all()
    serializer_class = ProgramStudiSerializer
    filterset_class = ProgramStudiFilter
