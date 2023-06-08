from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class SerializerContentType(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'
