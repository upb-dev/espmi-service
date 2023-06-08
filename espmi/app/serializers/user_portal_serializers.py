from espmi.app.models import Auditor, Fakultas, ProgramStudi, UnitPenunjang, UserPortal
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from espmi.app.serializers.auditor_serializers import AuditorSerializer
from espmi.app.serializers.fakultas_serializers import FakultasSerializer
from espmi.app.serializers.program_studi_serializers import ProgramStudiSerializer
from espmi.app.serializers.unit_penunjang_serializers import UnitPenunjangSerializer


class UserPortalSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField()

    class Meta:
        model = UserPortal
        fields = "__all__"

    def get_user_role(self, obj):
        serializer = None
        content_type = obj.content_type
        model = content_type.model_class()
        if model == Auditor:
            serializer = AuditorSerializer
        if model == Fakultas:
            serializer = FakultasSerializer
        if model == ProgramStudi:
            serializer = ProgramStudiSerializer
        if model == UnitPenunjang:
            serializer = UnitPenunjangSerializer
        serializer_instance = serializer(instance=obj.role)

        return serializer_instance.data
