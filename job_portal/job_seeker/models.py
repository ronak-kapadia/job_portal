from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=50)
    
class TimeStamp(models.Model):
    created_at  = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


class Jobseeker(TimeStamp):
    user = models.OneToOneField("User",on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField(unique = True, max_length=254)
    resume = models.FileField(upload_to='resumes/',max_length=100)
    skills = models.ManyToManyField(Skill, verbose_name=_(""))
    experience_years = models.PositiveIntegerField(default = 0)
  

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


