import django_filters
from espmi.app.models import RencanaTindakLanjut


class RencanaTindakLanjutFilter(django_filters.FilterSet):

    class Meta:
        model = RencanaTindakLanjut
        exclude = ['lampiran']
