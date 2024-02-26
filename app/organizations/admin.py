from django.contrib import admin

from organizations.models import Event
from organizations.models import Organization


class EventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
