from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


from .managers import MyUserManager




class MyUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_("Email_Address"), unique=True)
    username = models.CharField( max_length=100, unique=True)
    staff_id = models.CharField(default='FME/EAD/000', max_length=15)
    sign_up_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'staff_id']
    
    
    
    def __str__(self):
        return self.username
    
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
        
        
        


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
    
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_model(sender, instance, created, **kwargs):
    if created:
        StaffProfile.objects.create(user=instance)
    instance.staffprofile.save()