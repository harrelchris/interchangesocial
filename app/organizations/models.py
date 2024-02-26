from django.db import models

from common.models import BaseModel
from users.models import User


class Organization(BaseModel):
    name = models.CharField(max_length=512, unique=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_organizations", null=True)
    moderators = models.ManyToManyField(User, related_name="moderating_organizations")
    members = models.ManyToManyField(User, related_name="membership_organizations")

    def __str__(self):
        return self.name
