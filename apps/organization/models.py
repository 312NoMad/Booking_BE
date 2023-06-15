from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractModel

User = get_user_model()


class OrganizationType(AbstractModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("organization type")
        verbose_name_plural = _("organization types")


class Organization(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name=_("organization"))
    description = models.TextField(blank=True, null=True, verbose_name=_("description"))
    address = models.CharField(max_length=255, verbose_name=_("address"))
    type = models.ForeignKey(OrganizationType, on_delete=models.DO_NOTHING, verbose_name=_("organization type"))

    class Meta:
        verbose_name = _("organization")
        verbose_name_plural = _("organizations")

