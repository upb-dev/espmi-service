from espmi.app.models import SpmiGroup, Menu, SubMenu, GroupMenuRelation, GroupSubMenuRelation, UserBackOffice, UserPortal, ProgramStudi, Fakultas, UnitPenunjang, Auditor, KelompokSatuanMutu, SatuanMutu, StandarNasional, Standar, SubStandar
from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType


class GroupMenuInline(admin.StackedInline):
    model = GroupMenuRelation


class GroupSubMenuInline(admin.StackedInline):
    model = GroupSubMenuRelation


class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'description']

    filter_horizontal = ['permissions', 'menus']
    exclude = ['group_ptr']
    inlines = [GroupMenuInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('group_ptr')
        return queryset

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'permissions':
            kwargs['queryset'] = Permission.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)


class CustomMenuMenuAdmin(admin.ModelAdmin):
    inlines = [GroupSubMenuInline]


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', )


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.unregister(Group)
admin.site.register(ContentType)

admin.site.register(SpmiGroup, CustomGroupAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(GroupMenuRelation, CustomMenuMenuAdmin)
admin.site.register(GroupSubMenuRelation)
admin.site.register(ProgramStudi)
admin.site.register(Fakultas)
admin.site.register(UnitPenunjang)
admin.site.register(Auditor)
admin.site.register(UserBackOffice)
admin.site.register(UserPortal)
admin.site.register(SubStandar)
admin.site.register(Standar)
admin.site.register(SatuanMutu)
