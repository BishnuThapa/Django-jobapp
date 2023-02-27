from django.contrib import admin
from .models import Subscribe
# Register your models here.
# import export feature
from import_export.admin import ImportExportModelAdmin


@admin.register(Subscribe)
class SubscribeAdmin(ImportExportModelAdmin):
    list_display = ('email', 'option')
    list_editable = ('option',)
    list_per_page = 10
