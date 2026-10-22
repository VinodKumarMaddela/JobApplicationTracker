
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("applications/add/", views.add_application, name="add_application"),
    path(
        "applications/<int:pk>/edit/",
        views.edit_application,
        name="edit_application",
    ),
    
    path(
        "applications/<int:pk>/delete/",
        views.delete_application,
        name="delete_application",
    ),
    
    path(
        "api/applications/",
        views.JobApplicationListCreateAPIView.as_view(),
        name="api_applications",
    ),
    
    path(
        "api/applications/<int:pk>/",
        views.JobApplicationDetailAPIView.as_view(),
        name="api_application_detail",
    ),

]
