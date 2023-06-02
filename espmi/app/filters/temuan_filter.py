import django_filters
from espmi.app.models import Temuan


class TemuanFilter(django_filters.FilterSet):

    class Meta:
        model = Temuan
        exclude = ['lampiran']
