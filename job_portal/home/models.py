from django.db import models
from django.contrib.auth.models import User

class Employer(models.Model) :
    user = models.OneToOneField("User",on_delete=models.CASCADE)
    company = models.CharField(max_length=250)

    def __str__(self):
        return self.company
    
class Job(models.Model):
    employer =models.ForeignKey("Employer",on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_desc = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    experience = models.CharField(max_length=50)

    def __str__(self):
        return self.job_title
    
class JobSeeker(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')

class JobApplication(models.Model) :
    job = models.ForeignKey("Job",on_delete=models.CASCADE)
    job_seeker = models.ForeignKey("JobSeeker",on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"{self.job_seeker} applied for {self.job}"
    