
from rest_framework import generics
from .serializers import JobApplicationSerializer

from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import JobApplication
from .forms import JobApplicationForm


def dashboard(request):
    applications = JobApplication.objects.all()

    # Search by company, job title, or location
    search_query = request.GET.get("search", "").strip()
    if search_query:
        applications = applications.filter(
            models.Q(company_name__icontains=search_query)
            | models.Q(job_title__icontains=search_query)
            | models.Q(location__icontains=search_query)
        )

    # Filter by application status
    selected_status = request.GET.get("status", "").strip()
    valid_statuses = dict(JobApplication.STATUS_CHOICES)

    if selected_status in valid_statuses:
        applications = applications.filter(status=selected_status)
    else:
        selected_status = ""

    # Dashboard statistics always show all applications
    all_applications = JobApplication.objects.all()

    context = {
        "applications": applications,
        "search_query": search_query,
        "selected_status": selected_status,
        "status_choices": JobApplication.STATUS_CHOICES,
        "total_applications": all_applications.count(),
        "applied_count": all_applications.filter(status="APPLIED").count(),
        "interview_count": all_applications.filter(status="INTERVIEW").count(),
        "offer_count": all_applications.filter(status="OFFER").count(),
        "rejected_count": all_applications.filter(status="REJECTED").count(),
        "assessment_count": all_applications.filter(status="ASSESSMENT").count(),
    }

    return render(request, "applications/dashboard.html", context)


def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = JobApplicationForm()

    return render(
        request,
        "applications/application_form.html",
        {"form": form},
    )



def edit_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = JobApplicationForm(instance=application)

    return render(
        request,
        "applications/application_form.html",
        {
            "form": form,
            "is_edit": True,
        },
    )


def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == "POST":
        application.delete()
        return redirect("dashboard")

    return render(
        request,
        "applications/confirm_delete.html",
        {"application": application},
    )

def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == "POST":
        application.delete()
        return redirect("dashboard")

    return render(
        request,
        "applications/confirm_delete.html",
        {"application": application},
    )


class JobApplicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

class JobApplicationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
