# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class PaperDB(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True, verbose_name='번호')
    depart = models.TextField(blank=True, null=True, verbose_name='분야')
    depart_code = models.TextField(blank=True, null=True, verbose_name='분야 코드')
    title = models.TextField(blank=True, null=True, verbose_name='제목')
    author = models.TextField(blank=True, null=True, verbose_name='저자')
    journal = models.TextField(blank=True, null=True, verbose_name='학술지')
    date = models.TextField(blank=True, null=True, verbose_name='게재년월')
    sentence = models.TextField(blank=True, null=True, verbose_name='문장')
    search_cnt = models.BigIntegerField(blank=True, null=True, verbose_name='검색횟수')
    error_sentence = models.BooleanField(default=False, verbose_name='오류문장여부')

    class Meta:
        db_table = 'paperdb'


class Researchpart(models.Model):
    part_1_code = models.TextField(blank=True, null=True, verbose_name='최상위과학기술분류코드')
    part_1_name = models.TextField(blank=True, null=True, verbose_name='최상위과학기술분류코드한글명')
    part_2_code = models.TextField(blank=True, null=True, verbose_name='상위과학기술분류코드')
    part_2_name = models.TextField(blank=True, null=True, verbose_name='상위과학기술분류코드한글명')
    code = models.TextField(blank=True, null=True, verbose_name='과학기술분류코드')
    name = models.TextField(blank=True, null=True, verbose_name='연구분야')

    class Meta:
        db_table = 'researchpart'


class UserManager(BaseUserManager):

    def create_user(self, email, password, name, phone, interest, belong, rank, bachelor, master, doctor, auth,
                    **extra_fields):
        if not email:
            raise ValueError('email Required!')

        user = self.model(
            email=email,
            name=name,
            phone=phone,
            interest=interest,
            belong=belong,
            rank=rank,
            bachelor=bachelor,
            master=master,
            doctor=doctor,
            auth=auth,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name=None, phone=None, interest=None, belong=None, rank=None,
                         bachelor=None, master=None, doctor=None, auth=None):
        user = self.create_user(email, password, name, phone, interest, belong, rank, bachelor, master, doctor, auth)

        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(max_length=128, verbose_name="이메일", null=True, unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    name = models.CharField(max_length=128, verbose_name='이름')
    phone = models.CharField(max_length=128, blank=True, null=True, verbose_name='연락처')
    interest = models.CharField(max_length=256, blank=True, null=True, verbose_name='관심분야')
    belong = models.CharField(max_length=256, blank=True, null=True, verbose_name='소속')
    rank = models.CharField(max_length=256, blank=True, null=True, verbose_name='직위')
    bachelor = models.CharField(max_length=256, blank=True, null=True, verbose_name='학사')
    master = models.CharField(max_length=256, blank=True, null=True, verbose_name='석사')
    doctor = models.CharField(max_length=256, blank=True, null=True, verbose_name='박사')
    auth = models.CharField(max_length=10, blank=True, null=True, verbose_name='인증번호')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입일', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    last_login = models.DateTimeField(auto_now=True, verbose_name='마지막 로그인 날짜')

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_out = models.BooleanField(default=False, verbose_name='탈퇴여부')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"
