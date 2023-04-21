from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _



class MyUserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, email, username, staff_id, password, **extra_fields):
        
        if not email:
            raise ValueError(_(f"Please enter an email address"))
        
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, staff_id=staff_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    
    def create_superuser(self, email, username, staff_id, password, **extra_fields):
        
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be assigned to is_superuser=True')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned to is_staff=True')
        
        if extra_fields.get('is_admin') is not True:
            raise ValueError('superuser must be assigned to is_admin=True')
        
        return self.create_user(email, username, staff_id, password, **extra_fields)