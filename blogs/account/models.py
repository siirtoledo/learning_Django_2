# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# # Create your models here.



# # create your CustoomUserManager model here
# class CustomUserManager(BaseUserManager):
#     def _creae_user(self,email,password,first_name,last_name,mobile,**extrafields):
#         if not email:
#             raise ValueError("Email must be provided")
#         if not password:
#             raise ValueError("Password is not provided")
        
#         user=self.model(
#             email=self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#             mobile=mobile,
#             **extrafields
#         )
#         # this is aarshing password
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

#     def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)
#     # create your User Model here


# class User(AbstractBaseUser, PermissionsMixin):
#     # abstractbaseuser has password, last_login, is_active by default
#     email = models.EmailField(db_index=True, unique=True, max_length=254)
#     first_name = models.CharField(max_length=240)
#     last_name = models.CharField(max_length=255)
#     mobile = models.CharField(max_length=50)
#     address = models.CharField(max_length=250)

#     # must needed you wont be able to login in
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'


