from rest_framework import filters, viewsets
from espmi.app.serializers.content_type_serializer import SerializerContentType
from django.contrib.contenttypes.models import ContentType


class ContentTypeWiewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = SerializerContentType
