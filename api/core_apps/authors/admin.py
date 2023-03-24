from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "gender"]
    list_filter = ["gender"]
    list_display_links = ["id", "pkid"]


admin.site.register(Profile, ProfileAdmin)
