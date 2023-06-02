from django.db.transaction import atomic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.response import Response


class BaseModelViewSet(viewsets.ModelViewSet):
    serializer_class = None
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = '__all__'

    def paginate_queryset(self, queryset):
        if 'no_page' in self.request.query_params:
            return None

        return super().paginate_queryset(queryset)

    @atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response()

    @atomic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @atomic
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
