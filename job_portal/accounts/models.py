from django.db import models

from django.contrib.auth.models import AbstractBaseUser

class Accounts(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique = True, max_length=254)
    username  = models.CharField(max_length=50,unique = True)
    