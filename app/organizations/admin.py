from django.contrib import admin

from organizations.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)
