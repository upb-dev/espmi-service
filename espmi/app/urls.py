from rest_framework import routers
from django.urls import include, path
from espmi.app.views import menu_viewset, program_studi_viewset, satuan_mutu_viewset, unit_penujang_viewset, user_protal_viewset
from espmi.app.views.dokumen_type_viewset import DokumentTypeViewSet
from espmi.app.views.auditor_viewset import AuditorViewSet
from espmi.app.views.direktorat_viewset import DirektoratViewSet
from espmi.app.views.dokumen_category_viewset import DokumenCategoryViewSet
from espmi.app.views.dokumen_viewset import DokumenViewSet
from espmi.app.views.evaluasi_diri_viewset import EvaluasiDiriViewSet
from espmi.app.views.fakultas_viewset import FakultasViewSet
from espmi.app.views.indikator_viewset import IndikatorViewSet
from espmi.app.views.kelompok_satuan_mutu_viewset import KelompokSatuanMutuViewSet
from espmi.app.views.lembaga_akreditasi_viewset import LembagaAkreditasiViewSet
from espmi.app.views.nilai_mutu_viewset import NilaiMutuViewSet
from espmi.app.views.periode_viewset import PeriodeViewSet
from espmi.app.views.rektorat_viewset import RektoratViewSet
from espmi.app.views.rencana_tindak_lanjut_viewset import RencanaTindakLanjutViewSet
from espmi.app.views.spmi_group_viewset import SpmiGroupViewSet
from espmi.app.views.standar_nasional_viewset import StandarNasionalViewSet
from espmi.app.views.standar_viewset import StandarViewSet
from espmi.app.views.sub_menu_viewset import SubMenuViewSet
from espmi.app.views.sub_standar_viewset import SubStandarViewSet
from espmi.app.views.tahun_periode_viewset import TahunPeriodeViewSet
from espmi.app.views.target_nilai_mutu_viewset import TargetNilaiMutuViewSet
from espmi.app.views.temuan_viewset import TemuanViewSet
from espmi.app.views.user_backoffice_viewset import UserBackOfficeViewSet
from espmi.app.views.visitasi_viewset import VisitasiViewSet
router = routers.DefaultRouter()
router.register(r'auditor', AuditorViewSet)
router.register(r'direktorat', DirektoratViewSet)
router.register(r'dokumen-category', DokumenCategoryViewSet)
router.register(r'dokumen-type', DokumentTypeViewSet)
router.register(r'dokumen', DokumenViewSet)
router.register(r'evaluasi-diri', EvaluasiDiriViewSet)
router.register(r'fakultas', FakultasViewSet)
router.register(r'indikator', IndikatorViewSet)
router.register(r'kelompok-satuan-mutu', KelompokSatuanMutuViewSet)
router.register(r'lambaga-akreditasi', LembagaAkreditasiViewSet)
router.register(r'menu', menu_viewset.MenuViewSet)
router.register(r'nilai-mutu', NilaiMutuViewSet)
router.register(r'periode', PeriodeViewSet)
router.register(r'program-studi', program_studi_viewset.ProgramStudiViewSet)
router.register(r'rektorat', RektoratViewSet)
router.register(r'renacna-tindak-lanjut', RencanaTindakLanjutViewSet)
router.register(r'spmi-group', SpmiGroupViewSet)
router.register(r'satuan-mutu', satuan_mutu_viewset.SatuanMutuViewSet)
router.register(r'standar-nasional', StandarNasionalViewSet)
router.register(r'standar', StandarViewSet)
router.register(r'sub-menu', SubMenuViewSet)
router.register(r'sub-standar', SubStandarViewSet)
router.register(r'tahun-periode', TahunPeriodeViewSet)
router.register(r'target-nilai-mutu', TargetNilaiMutuViewSet)
router.register(r'temuan', TemuanViewSet)
router.register(r'unit-penujang', unit_penujang_viewset.UnitPenunjangViewSet)
router.register(r'user-backoffice', UserBackOfficeViewSet)
router.register(r'user-portal', user_protal_viewset.UserPortalViewSet)
router.register(r'visitasi', VisitasiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
