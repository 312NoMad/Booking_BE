from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.models import AbstractModel


class DictionaryModel(AbstractModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Country(DictionaryModel):
    pass

    class Meta:
        verbose_name = _("country")
        verbose_name_plural = _("countries")


class City(DictionaryModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities", verbose_name=_("city"))

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")


class Street(DictionaryModel):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="streets", verbose_name=_("street"))

    class Meta:
        verbose_name = _("street")
        verbose_name_plural = _("streets")


class Location(AbstractModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="locations", verbose_name=_("country"))
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="cities", verbose_name=_("city"))
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name="streets", verbose_name=_("street"))
    number = models.CharField(max_length=10)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_("longitude"))
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_("latitude"))

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return f"{self.street} {self.number}, {self.city}, {self.country} ({self.longitude}, {self.latitude})"
