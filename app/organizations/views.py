from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from organizations.models import Organization


class OrganizationListView(ListView):
    context_object_name = "organizations"
    model = Organization
    template_name = "organizations/list.html"


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    template_name = "organizations/create.html"
    fields = [
        "name",
    ]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        self.object.moderators.add(self.request.user)
        self.object.members.add(self.request.user)
        return redirect(to=reverse_lazy(viewname="organization:detail", kwargs={"name": self.object.name}))


class OrganizationDetailView(DetailView):
    context_object_name = "organization"
    model = Organization
    template_name = "organizations/detail.html"

    def get_object(self, queryset=None):
        return Organization.objects.get(name=self.kwargs.get("name"))
