import uuid

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        Group, PermissionsMixin)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


# Create your models here.
class BaseFieldModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    class Meta:
        abstract = True


class BaseEntryModel(BaseFieldModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        if password:
            extra_fields['password'] = make_password(password)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class GroupCustomUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    custom_user = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group} - {self.custom_user}"


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    oauth_id = models.UUIDField(null=True, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True)
    group = models.ForeignKey("SpmiGroup", on_delete=models.SET_NULL, null=True, related_name='users')

    groups = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save_oauth_id(self, oauth_id):
        self.oauth_id = oauth_id
        self.save()

    def update_last_login(self):
        self.last_login_at = timezone.now()
        self.save()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.email}'

    def get_short_name(self):
        return self.email


class BaseModel(BaseEntryModel):
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_createdby",
                                   null=True, on_delete=models.SET_NULL, blank=True)
    updated_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_updatedby",
                                   null=True, on_delete=models.SET_NULL, blank=True)

    class Meta:
        abstract = True


class UserBackOffice(User):
    full_name = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.pk is None:
            # Jika objek baru, panggil set_password() untuk meng-hash password
            self.set_password(self.password)
        super().save(*args, **kwargs)


class UserPortal(User):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    role_id = models.UUIDField()
    role = GenericForeignKey('content_type', 'role_id')

    def save(self, *args, **kwargs):
        if self.pk is None:
            # Jika objek baru, panggil set_password() untuk meng-hash password
            self.set_password(self.password)
        super().save(*args, **kwargs)


class SpmiGroup(Group):
    UNIT_TYPE = [
        (1, 'PUSAT'),
        (2, 'PORTAL'),
    ]
    description = models.CharField(max_length=255, null=True)
    unit = models.IntegerField(choices=UNIT_TYPE)
    menus = models.ManyToManyField("Menu", through="GroupMenuRelation")
    permissions = None

    class Meta:

        verbose_name_plural = 'SPMI Groups'

    def __str__(self):
        return self.name


class Menu(BaseEntryModel):
    name = models.CharField(max_length=255)
    UNIT_CHOICE = [
        (1, 'PUSAT'),
        (2, 'PORTAL'),
    ]
    unit_type = models.IntegerField(choices=UNIT_CHOICE)

    # Tambahkan field lain yang diperlukan

    def __str__(self):
        return self.name


class GroupMenuRelation(BaseEntryModel):
    group = models.ForeignKey(SpmiGroup, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    submenus = models.ManyToManyField("SubMenu", through="GroupSubMenuRelation")
    # Tambahkan field lain yang diperlukan

    def __str__(self):
        return f"Group: {self.group.name} - Menu: {self.menu.name}"


class GroupSubMenuRelation(models.Model):
    group_menu_relation = models.ForeignKey(GroupMenuRelation, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    submenu = models.ForeignKey("SubMenu", on_delete=models.CASCADE)
    # Tambahkan field lain yang diperlukan

    def __str__(self):
        return f"GroupMenuRelation: {self.group_menu_relation.id} - SubMenu: {self.submenu.name}"


class SubMenu(BaseEntryModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # Tambahkan field lain yang diperlukan

    def __str__(self):
        return self.name


class Auditor(BaseEntryModel):
    nik = models.CharField(max_length=50, unique=True)
    gelar_depan = models.CharField(max_length=5, blank=True)
    nama_lengkap = models.CharField(max_length=100)
    lembaga_akreditasi_id = models.ForeignKey(to="LembagaAkreditasi", null=True, on_delete=models.CASCADE)
    gelar_belakang = models.CharField(max_length=30, blank=True)
    gender = models.IntegerField(choices=[(1, "Laki-Laki"), (2, "Perempuan")])
    instansi = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    units_id = models.ManyToManyField(to="Unit")


class DocumentCategory(BaseEntryModel):
    name = models.CharField(max_length=255)


def __str__(self):
    return self.name


class DocumentType(BaseEntryModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to=DocumentCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dokumen(BaseModel):
    type = models.ForeignKey(to=DocumentType, on_delete=models.CASCADE)
    # pogram_studi = models.ForeignKey(to="ProgramStudi", on_delete=models.CASCADE, null=True)  # TODO delete relasi
    name = models.CharField(max_length=255)
    tahun = models.IntegerField()
    file = models.FileField(upload_to='dokumen/')

    def __str__(self):
        return self.name


class Unit(BaseEntryModel):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Fakultas(Unit):
    pass


class Rektorat(Unit):
    code = models.CharField(max_length=5)
    address = models.TextField()
    desc = models.TextField()


class Direktorat(Unit):
    code = models.CharField(max_length=5)
    address = models.TextField()
    desc = models.TextField()


class UnitPenunjang(BaseEntryModel):
    code = models.CharField(max_length=5)
    address = models.TextField()
    desc = models.TextField()


class ProgramStudi(Unit):
    AKREDITAS_TYPE = [
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'Baik Sekali'),
        (5, 'Unggul'),
    ]
    code = models.CharField(max_length=10)
    fakultas_rel = models.ForeignKey(to=Fakultas, on_delete=models.CASCADE, related_name='program_studi_set')
    akreditasi_type = models.IntegerField(choices=AKREDITAS_TYPE)
    no_sk = models.CharField(max_length=255)
    start_akreditasi = models.DateField()
    end_akreditasi = models.DateField()
    file_akreditasi = models.FileField(upload_to='upload/')
    address = models.TextField(blank=True)
    desc = models.TextField(blank=True)


class LembagaAkreditasi(BaseEntryModel):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)


class StandarNasional(BaseEntryModel):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)


class StandarNasionalPeriodeRelation(models.Model):
    standar_nasional = models.ForeignKey(to=StandarNasional, on_delete=models.CASCADE)
    periode = models.ForeignKey(to="Periode", on_delete=models.CASCADE)


class TahunPeriode(BaseEntryModel):
    tahun = models.IntegerField()
    is_active = models.BooleanField(default=True)


class Periode(BaseEntryModel):
    tahun = models.ForeignKey(to=TahunPeriode, on_delete=models.CASCADE)
    lembaga_akreditasi = models.ForeignKey(to=LembagaAkreditasi, on_delete=models.CASCADE)
    standar_nasional = models.ManyToManyField(StandarNasional, through=StandarNasionalPeriodeRelation)
    start_evaluasi_diri = models.DateField()
    end_evaluasi_diri = models.DateField()
    start_desk_evaluation = models.DateField()
    end_desk_evaluation = models.DateField()
    start_visitasi = models.DateField()
    end_visitasi = models.DateField()

    def clean(self):
        if self.start_evaluasi_diri and self.end_evaluasi_diri:
            if self.start_evaluasi_diri > self.end_evaluasi_diri:
                raise ValidationError('Tanggal mulai tidak dapat lebih besar dari tanggal berakhir.')
        if self.start_desk_evaluation and self.end_desk_evaluation:
            if self.start_desk_evaluation > self.end_desk_evaluation:
                raise ValidationError('Tanggal mulai tidak dapat lebih besar dari tanggal berakhir.')
        if self.start_visitasi and self.end_visitasi:
            if self.start_visitasi > self.end_visitasi:
                raise ValidationError('Tanggal mulai tidak dapat lebih besar dari tanggal berakhir.')


class TargetNilaiMutu(BaseEntryModel):
    program_studi = models.ForeignKey(to=ProgramStudi, on_delete=models.CASCADE)
    tahun = models.ForeignKey(to=TahunPeriode, on_delete=models.CASCADE)
    lembaga_akreditasi = models.ForeignKey(to=LembagaAkreditasi, on_delete=models.CASCADE)
    nilai_target = models.FloatField()
    desc = models.TextField()


class NilaiMutu(BaseEntryModel):
    tahun = models.ForeignKey(to=TahunPeriode, on_delete=models.CASCADE)
    lembaga_akreditasi = models.ForeignKey(to=LembagaAkreditasi, on_delete=models.CASCADE)
    nilai_mutu = models.FloatField()
    desc = models.TextField()


class BaseMutu(BaseModel):
    tahun = models.ForeignKey(TahunPeriode, on_delete=models.CASCADE)
    lembaga_akreditasi = models.ForeignKey(LembagaAkreditasi, on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    data_dukung = models.TextField(blank=True)
    jenjang = models.ManyToManyField(to=Unit)
    desc = models.TextField(blank=True)
    jenis_indikator = models.IntegerField(choices=[(1, 'Kuantitatif'), (2, 'Kualitatif'), (3, 'Radio')], default=1)
    bobot_nilai = models.FloatField(null=True)

    class Meta:
        abstract = True


class KelompokSatuanMutu(BaseMutu):
    pass


class SatuanMutu(BaseMutu):
    kelompok_satuan_mutu = models.ForeignKey(KelompokSatuanMutu, on_delete=models.CASCADE)


class Standar(BaseMutu):
    satuan_mutu = models.ForeignKey(SatuanMutu, on_delete=models.CASCADE)


class SubStandar(BaseMutu):
    standar = models.ForeignKey(Standar, on_delete=models.CASCADE)
    plotting_unit_kerja = models.ManyToManyField(Unit, related_name="substandar_plotting_unit_kerja")


class Indikator(BaseEntryModel):
    sub_standar = models.ForeignKey(SubStandar, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.FloatField()
    data = models.TextField()


class Temuan(BaseModel):
    sub_standar = models.ForeignKey(to=SubStandar, on_delete=models.CASCADE)
    daftar_temuan = models.TextField()
    jenis_temuan = models.IntegerField(choices=[(1, "Observasi / Minor"), (2, "KTS / Mayor")])
    akar_masalah = models.TextField()
    rekomendasi = models.TextField()
    peningkatan = models.TextField(blank=True)
    lampiran = models.FileField(upload_to="upload/")


class RencanaTindakLanjut(BaseModel):
    temuan = models.ForeignKey(to=Temuan, on_delete=models.CASCADE)
    rencana_aksi = models.TextField(blank=True)
    penanggung_jawab = models.TextField(blank=True)
    target_penyelesaian = models.TextField(blank=True)
    status = models.IntegerField(choices=[(1, "Belum"), (2, "Sudah")])
    lampiran = models.FileField(upload_to='upload/')


class Visitasi(BaseModel):
    sub_standar = models.ForeignKey(to=SubStandar, on_delete=models.CASCADE)
    indikator = models.ForeignKey(to=Indikator, on_delete=models.CASCADE)


class EvaluasiDiri(BaseModel):
    sub_standar = models.ForeignKey(to=SubStandar, on_delete=models.CASCADE)
    indikator = models.ForeignKey(to=Indikator, on_delete=models.CASCADE)
    dokumen = models.ManyToManyField(to=Dokumen)

# TODO history evaluasi diri
