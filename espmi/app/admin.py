from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from espmi.app.models import (Auditor, Direktorat, DocumentCategory, DocumentType, Dokumen, EvaluasiDiri, Fakultas, GroupMenuRelation,
                              GroupSubMenuRelation, Indikator, KelompokSatuanMutu, LembagaAkreditasi, Menu, NilaiMutu, Periode,
                              ProgramStudi, Rektorat, RencanaTindakLanjut, SatuanMutu, SpmiGroup, Standar,
                              StandarNasional, SubMenu, SubStandar, TahunPeriode, TargetNilaiMutu, Temuan, Unit, User,
                              UnitPenunjang, UserBackOffice, UserPortal, Visitasi)


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


class AuditorUnitInline(admin.StackedInline):
    model = Unit


class CustomAuditorAdmin(admin.ModelAdmin):
    list_display = ['nik', 'nama_lengkap', 'instansi', 'jabatan']
    filter_horizontal = ['units_id']
    # inlines =


class CustomMenuMenuAdmin(admin.ModelAdmin):
    inlines = [GroupSubMenuInline]


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', )


class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DokumenTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_id']


class DokumenCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.unregister(Group)
admin.site.register(ContentType)

admin.site.register(Auditor, CustomAuditorAdmin)
admin.site.register(Direktorat)
admin.site.register(DocumentCategory, DokumenCategoryAdmin)
admin.site.register(DocumentType, DokumenTypeAdmin)
admin.site.register(Dokumen)

admin.site.register(SpmiGroup, CustomGroupAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, SubMenuAdmin)
admin.site.register(GroupMenuRelation, CustomMenuMenuAdmin)
admin.site.register(GroupSubMenuRelation)
admin.site.register(ProgramStudi)
admin.site.register(Fakultas)
admin.site.register(UnitPenunjang)
admin.site.register(UserBackOffice)
admin.site.register(UserPortal)
admin.site.register(SubStandar)
admin.site.register(Standar)
admin.site.register(SatuanMutu)
admin.site.register(User)
admin.site.register(Temuan)
admin.site.register(Visitasi)
admin.site.register(EvaluasiDiri)
admin.site.register(RencanaTindakLanjut)
admin.site.register(Indikator)
admin.site.register(KelompokSatuanMutu)
admin.site.register(NilaiMutu)
admin.site.register(TargetNilaiMutu)
admin.site.register(Periode)
admin.site.register(LembagaAkreditasi)
admin.site.register(Rektorat)
admin.site.register(Unit)
admin.site.register(StandarNasional)
admin.site.register(TahunPeriode)
