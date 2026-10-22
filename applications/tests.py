from django.urls import reverse
from datetime import date

from django.test import TestCase
from .models import JobApplication


class JobApplicationModelTests(TestCase):
    def setUp(self):
        self.application = JobApplication.objects.create(
            company_name="Test Technologies",
            job_title="Python Developer",
            location="Hyderabad",
            status="APPLIED",
            applied_date=date.today(),
            salary="4-6 LPA",
            notes="Automated test application",
        )

    def test_application_is_created(self):
        self.assertEqual(
            JobApplication.objects.count(),
            1,
        )

    def test_application_string_representation(self):
        self.assertEqual(
            str(self.application),
            "Python Developer at Test Technologies",
        )

    def test_default_ordering(self):
        self.assertEqual(
            JobApplication.objects.first(),
            self.application,
        )



class JobApplicationViewTests(TestCase):
    def test_dashboard_loads_successfully(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "applications/dashboard.html",
        )

    def test_add_application_page_loads(self):
        response = self.client.get(reverse("add_application"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "applications/application_form.html",
        )