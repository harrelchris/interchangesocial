from django.urls import path

from organizations import views

app_name = "organization"

urlpatterns = [
    path("", views.OrganizationListView.as_view(), name="list"),
    path("create/", views.OrganizationCreateView.as_view(), name="create"),
    path("<str:name>/", views.OrganizationDetailView.as_view(), name="detail"),
]
