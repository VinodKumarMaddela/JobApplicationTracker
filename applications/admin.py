
from django.contrib import admin
from .models import JobApplication


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "job_title",
        "status",
        "applied_date",
        "location",
        "created_at",
    )

    list_filter = ("status", "applied_date")
    search_fields = ("company_name", "job_title", "location")
    ordering = ("-created_at",)
    date_hierarchy = "applied_date"

    list_per_page = 20
