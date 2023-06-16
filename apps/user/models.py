from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string

from utils.models import AbstractModel


GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other")
)


class User(AbstractUser, PermissionsMixin, AbstractModel):
    is_active = models.BooleanField(default=False, verbose_name=_("is active"))
    activation_code = models.CharField(max_length=10, default=get_random_string(10))

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def create_activation_code(self):
        code = get_random_string(20)
        self.activation_code = code
        self.save()
        return code


class Customer(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name=_("customer"))
    description = models.TextField(blank=True, null=True, verbose_name=_("description"))
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")
