from espmi.app.models import GroupMenuRelation, GroupSubMenuRelation, SpmiGroup
from rest_framework import serializers


class GroupSubMenuRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSubMenuRelation
        fields = '__all__'


class GroupMenuRelationSerializer(serializers.ModelSerializer):
    group_sub_menu = GroupSubMenuRelationSerializer(many=True, source="groupsubmenurelation_set")

    class Meta:
        model = GroupMenuRelation
        fields = '__all__'


class SpmiGroupSerializer(serializers.ModelSerializer):
    group_menu = GroupMenuRelationSerializer(many=True, source="groupmenurelation_set")

    class Meta:
        model = SpmiGroup
        fields = "__all__"
