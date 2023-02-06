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
    search_fields = ('title', 'salary',)
    search_help_text = "Write in your query & hit enter"
    # fields = (('title', 'slug'), 'description')
    # exclude = ('posted_date',)

    # fieldset options
    # - (name,field_options)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug')
        }),
        ('More Information', {
            'classes': ('collapse',),
            'fields': ('description', 'salary', 'expiry')
        }),
    )
