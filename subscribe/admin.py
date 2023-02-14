from django.contrib import admin
from .models import Subscribe
# Register your models here.


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'option')
    list_editable = ('option',)
    list_per_page = 10
