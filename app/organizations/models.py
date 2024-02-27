from django.db import models
from django.urls import reverse_lazy

from common.models import BaseModel
from users.models import User


class Organization(BaseModel):
    name = models.CharField(max_length=512, unique=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_organizations", null=True)
    moderators = models.ManyToManyField(User, related_name="moderating_organizations")
    members = models.ManyToManyField(User, related_name="membership_organizations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("organizations:detail", kwargs={"organization_name": self.name})


class Event(BaseModel):
    name = models.CharField(max_length=512)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_events", null=True)
    moderators = models.ManyToManyField(User, related_name="moderating_events")
    members = models.ManyToManyField(User, related_name="membership_events")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy(
            "organizations:event_detail",
            kwargs={
                "organization_name": self.organization.name,
                "event_name": self.name
            }
        )
