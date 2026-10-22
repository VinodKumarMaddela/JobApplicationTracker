from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import JobApplication
from .forms import JobApplicationForm
from .serializers import JobApplicationSerializer


@login_required
def dashboard(request):
    # Show only applications belonging to the logged-in user.
    all_applications = JobApplication.objects.filter(owner=request.user)
    applications = all_applications

    search_query = request.GET.get("search", "").strip()
    if search_query:
        applications = applications.filter(
            models.Q(company_name__icontains=search_query)
            | models.Q(job_title__icontains=search_query)
            | models.Q(location__icontains=search_query)
        )

    selected_status = request.GET.get("status", "").strip()
    valid_statuses = dict(JobApplication.STATUS_CHOICES)

    if selected_status in valid_statuses:
        applications = applications.filter(status=selected_status)
    else:
        selected_status = ""

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


@login_required
def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.owner = request.user
            application.save()
            return redirect("dashboard")
    else:
        form = JobApplicationForm()

    return render(
        request,
        "applications/application_form.html",
        {"form": form},
    )


@login_required
def edit_application(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk,
        owner=request.user,
    )

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
        {"form": form, "is_edit": True},
    )


@login_required
def delete_application(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        application.delete()
        return redirect("dashboard")

    return render(
        request,
        "applications/confirm_delete.html",
        {"application": application},
    )


class JobApplicationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class JobApplicationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return JobApplication.objects.filter(owner=self.request.user)

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your account has been created successfully. Please sign in."
            )
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form},
    )