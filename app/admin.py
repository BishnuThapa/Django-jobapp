from django.contrib import admin
from .models import JobPost
# Register your models here.


# admin.site.register(JobPost)
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
