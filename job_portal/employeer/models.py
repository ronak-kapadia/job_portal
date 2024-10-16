from django.db import models


class Employeer(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length = 300)
    email = models.EmailField(max_length=300,unique = True)
    username  = models.CharField(max_length=50,unique = True)
    company_name  = models.CharField(max_length = 250)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

    