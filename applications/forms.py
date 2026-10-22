
from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            "company_name",
            "job_title",
            "job_url",
            "location",
            "status",
            "applied_date",
            "salary",
            "notes",
        ]

        widgets = {
            "company_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "job_title": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "job_url": forms.URLInput(
                attrs={"class": "form-control"}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
            "applied_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "salary": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
        }
