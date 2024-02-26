from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import include
from django.urls import path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("public.urls"), name="public"),
    path("organizations/", include("organizations.urls"), name="organizations"),
]

admin.site.login = staff_member_required(admin.site.login, login_url=settings.LOGIN_URL)
admin.site.index_title = settings.ADMIN_INDEX_TITLE
admin.site.name = settings.ADMIN_NAME
admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
