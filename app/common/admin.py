from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required

admin.site.index_title = "Site administration"
admin.site.name = "admin"
admin.site.site_header = "Django administration"
admin.site.site_title = "Site administration"

admin.site.login = staff_member_required(
    admin.site.login, login_url=settings.LOGIN_URL
)
