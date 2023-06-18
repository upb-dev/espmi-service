import django_filters
from espmi.app.models import NilaiMutu


class NilaiMutuFilter(django_filters.FilterSet):
    tahun = django_filters.CharFilter(field_name='tahun__tahun')
    lembaga = django_filters.CharFilter(field_name='lembaga_akreditasi__name')

    class Meta:
        model = NilaiMutu
        exclude = []
