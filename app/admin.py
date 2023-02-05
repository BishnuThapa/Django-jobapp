from django.contrib import admin
from .models import JobPost
# Register your models here.


# admin.site.register(JobPost)
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title',  'salary', 'posted_date',)
    list_editable = ('salary',)
    list_filter = ('posted_date', 'salary', 'expiry',)
