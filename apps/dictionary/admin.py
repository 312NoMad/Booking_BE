from django.contrib import admin

from .models import Country, City, Street


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

    class CityInline(admin.TabularInline):
        model = City

    inlines = [CityInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    class StreetInline(admin.TabularInline):
        model = Street

    inlines = [StreetInline]


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    pass
