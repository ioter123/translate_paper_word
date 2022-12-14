# Generated by Django 4.1 on 2022-11-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperDB',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='번호')),
                ('depart', models.TextField(blank=True, null=True, verbose_name='분야')),
                ('depart_code', models.TextField(blank=True, null=True, verbose_name='분야 코드')),
                ('title', models.TextField(blank=True, null=True, verbose_name='제목')),
                ('author', models.TextField(blank=True, null=True, verbose_name='저자')),
                ('journal', models.TextField(blank=True, null=True, verbose_name='학술지')),
                ('date', models.TextField(blank=True, null=True, verbose_name='게재년월')),
                ('sentence', models.TextField(blank=True, null=True, verbose_name='문장')),
                ('search_cnt', models.BigIntegerField(blank=True, null=True, verbose_name='검색횟수')),
                ('error_sentence', models.BooleanField(default=False, verbose_name='오류문장여부')),
            ],
            options={
                'db_table': 'paperdb',
            },
        ),
        migrations.CreateModel(
            name='Researchpart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_1_code', models.TextField(blank=True, null=True, verbose_name='최상위과학기술분류코드')),
                ('part_1_name', models.TextField(blank=True, null=True, verbose_name='최상위과학기술분류코드한글명')),
                ('part_2_code', models.TextField(blank=True, null=True, verbose_name='상위과학기술분류코드')),
                ('part_2_name', models.TextField(blank=True, null=True, verbose_name='상위과학기술분류코드한글명')),
                ('code', models.TextField(blank=True, null=True, verbose_name='과학기술분류코드')),
                ('name', models.TextField(blank=True, null=True, verbose_name='연구분야')),
            ],
            options={
                'db_table': 'researchpart',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, null=True, unique=True, verbose_name='이메일')),
                ('password', models.CharField(max_length=256, verbose_name='비밀번호')),
                ('name', models.CharField(max_length=128, verbose_name='이름')),
                ('phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='연락처')),
                ('interest', models.CharField(blank=True, max_length=256, null=True, verbose_name='관심분야')),
                ('belong', models.CharField(blank=True, max_length=256, null=True, verbose_name='소속')),
                ('rank', models.CharField(blank=True, max_length=256, null=True, verbose_name='직위')),
                ('bachelor', models.CharField(blank=True, max_length=256, null=True, verbose_name='학사')),
                ('master', models.CharField(blank=True, max_length=256, null=True, verbose_name='석사')),
                ('doctor', models.CharField(blank=True, max_length=256, null=True, verbose_name='박사')),
                ('auth', models.CharField(blank=True, max_length=10, null=True, verbose_name='인증번호')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='가입일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='마지막 로그인 날짜')),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_out', models.BooleanField(default=False, verbose_name='탈퇴여부')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'user',
            },
        ),
    ]
