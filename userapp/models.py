from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser




class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("User Must have email")
        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password=None):
        if not password:
            raise ValueError("Superusers must have password")
        user=self.create_user(email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user



class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True,  editable=False)
    name=models.CharField(verbose_name="User_Name",max_length=30)
    email=models.EmailField(verbose_name="Email",max_length=50,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = []
    objects=UserManager()

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    def has_module_perms(self,applabel):
        return True
