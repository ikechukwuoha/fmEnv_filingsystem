from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


from .managers import MyUserManager


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email_Address"), unique=True)
    username = models.CharField(max_length=100, unique=True)
    staff_id = models.CharField(default="FME/EAD/000", max_length=15, unique=True)
    sign_up_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "staff_id"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STAFF = "STAFF", "Staff"
        GIS_STAFF = "GIS_STAFF", "Gis_staff"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=MyUser.Role.STAFF)


class Staff(MyUser):
    base_role = MyUser.Role.STAFF

    staff = StaffManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Staffs Only"


class StaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    rank = models.CharField(max_length=6)
    department = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        """
        This Function returns the first name, midle name and last name with space in between
        """
        full_name = f"{self.first_name} {self.other_name} {self.last_name}"
        return full_name()

    def short_name(self):
        """This Function returns Just the first name..."""
        short_name = f"{self.first_name}"
        return short_name()


@receiver(post_save, sender=Staff)
def create_staff_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STAFF":
        StaffProfile.objects.create(user=instance)


class GISStaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=MyUser.Role.GIS_STAFF)


class Gis_staff(MyUser):
    base_role = MyUser.Role.GIS_STAFF

    gis_staff = GISStaffManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "GIS Staffs Only"


class GisStaffProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    rank = models.CharField(max_length=6)
    department = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        """
        This Function returns the first name, midle name and last name with space in between
        """
        full_name = f"{self.first_name} {self.other_name} {self.last_name}"
        return full_name()

    def short_name(self):
        """This Function returns Just the first name..."""
        short_name = f"{self.first_name}"
        return short_name()


@receiver(post_save, sender=Gis_staff)
def save_user_model(sender, instance, created, **kwargs):
    if created and instance.role == "GIS_STAFF":
        GisStaffProfile.objects.create(user=instance)
