from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


# Register your models here.
@admin.register(PaperDB)
class PaperDB(admin.ModelAdmin):
    list_display = (
        'depart',
        'depart_code',
        'title',
        'author',
        'journal',
        'date',
        'sentence',
        'search_cnt',
        'error_sentence',
    )
    list_display_links = (
        'depart',
        'depart_code',
        'title',
        'author',
        'journal',
        'date',
        'sentence',
        'search_cnt',
        'error_sentence',
    )

    search_fields = [
        'depart',
        'depart_code',
        'title',
        'author',
        'journal',
        'date',
        'sentence',
        'search_cnt',
        'error_sentence',
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'password',
        'name',
        'phone',
        'interest',
        'belong',
        'rank',
        'bachelor',
        'master',
        'doctor',
        'is_active',
        'created_at',
        'updated_at',
        'last_login',
        'is_out',
    )
    list_display_links = (
        'email',
        'password',
        'name',
        'phone',
        'interest',
        'belong',
        'rank',
        'bachelor',
        'master',
        'doctor',
        'is_active',
        'created_at',
        'updated_at',
        'last_login',
        'is_out',
    )

    search_fields = [
        'email',
        'password',
        'name',
        'phone',
        'interest',
        'belong',
        'rank',
        'bachelor',
        'master',
        'doctor',
        'is_active',
        'created_at',
        'updated_at',
        'last_login',
        'is_out',
    ]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
