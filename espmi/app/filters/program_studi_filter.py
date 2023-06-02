import django_filters
from espmi.app.models import ProgramStudi


class ProgramStudiFilter(django_filters.FilterSet):

    class Meta:
        model = ProgramStudi
        exclude = ['file_akreditasi']
