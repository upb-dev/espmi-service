import django_filters
from espmi.app.models import Dokumen


class DokumenFilter(django_filters.FilterSet):

    class Meta:
        model = Dokumen
        exclude = ['file']
