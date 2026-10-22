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
from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import JobApplication


User = get_user_model()


class JobApplicationModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword!234",
        )
        self.application = JobApplication.objects.create(
            owner=self.user,
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
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPassword!234",
        )
        self.client.force_login(self.user)

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

class JobApplicationOwnershipTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="owner1",
            password="TestPassword!234",
        )
        self.user2 = User.objects.create_user(
            username="owner2",
            password="TestPassword!234",
        )

        self.application = JobApplication.objects.create(
            owner=self.user1,
            company_name="Private Company",
            job_title="Python Developer",
            status="APPLIED",
            applied_date=date.today(),
        )

    def test_dashboard_shows_only_own_applications(self):
        self.client.force_login(self.user2)

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Private Company")
        self.assertEqual(response.context["total_applications"], 0)

    def test_user_cannot_edit_another_users_application(self):
        self.client.force_login(self.user2)

        response = self.client.get(
            reverse("edit_application", args=[self.application.pk])
        )

        self.assertEqual(response.status_code, 404)

    def test_user_cannot_delete_another_users_application(self):
        self.client.force_login(self.user2)

        response = self.client.get(
            reverse("delete_application", args=[self.application.pk])
        )

        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            JobApplication.objects.filter(pk=self.application.pk).exists()
        )

    def test_api_list_shows_only_own_applications(self):
        self.client.force_login(self.user2)

        response = self.client.get(reverse("api_applications"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"] if isinstance(response.data, dict) and "results" in response.data else response.data, [])
