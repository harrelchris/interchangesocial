from django.urls import path

from organizations import views

app_name = "organizations"

urlpatterns = [
    path("", views.OrganizationListView.as_view(), name="list"),
    path("create/", views.OrganizationCreateView.as_view(), name="create"),
    path("<str:organization_name>/", views.OrganizationDetailView.as_view(), name="detail"),
    path("<str:organization_name>/events/create/", views.EventCreateView.as_view(), name="event_create"),
    path("<str:organization_name>/events/<str:event_name>/", views.EventDetailView.as_view(), name="event_detail"),
]
