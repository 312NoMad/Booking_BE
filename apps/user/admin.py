from django.contrib import admin

from .models import User, Customer


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
