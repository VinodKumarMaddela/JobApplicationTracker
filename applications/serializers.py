
from rest_framework import serializers
from .models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = JobApplication
        fields = [
            "id",
            "owner",
            "company_name",
            "job_title",
            "job_url",
            "location",
            "status",
            "applied_date",
            "salary",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
        ]
