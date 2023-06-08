from rest_framework import serializers

from espmi.app.models import (GroupMenuRelation, GroupSubMenuRelation, Menu,
                              SpmiGroup)


class MenuGroupSerializer(serializers.ModelSerializer):
    unit = serializers.CharField(read_only=True, source="get_unit_type_display")

    class Meta:
        model = Menu
        fields = ['name', 'unit']


class GroupSubMenuRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSubMenuRelation
        fields = ['active', 'submenu']


class GroupMenuRelationSerializer(serializers.ModelSerializer):
    group_sub_menu = GroupSubMenuRelationSerializer(read_only=True, many=True, source="groupsubmenurelation_set")
    # menu = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Menu.objects.all())
    menu_data = MenuGroupSerializer(read_only=True, source='menu')

    class Meta:
        model = GroupMenuRelation
        fields = ['active', 'group_sub_menu', "menu_data"]


class SpmiGroupSerializer(serializers.ModelSerializer):
    group_menu = GroupMenuRelationSerializer(read_only=True, many=True, source="groupmenurelation_set")

    class Meta:
        model = SpmiGroup
        fields = ['id', 'name', 'unit', 'description', 'group_menu']
