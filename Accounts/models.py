from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Country = models.CharField(max_length=50)
    Profession = models.CharField(max_length=50)
    Description = models.TextField(max_length=1000, null=False, blank=False)
    Github_link = models.URLField(null=True, blank=True)
    Linkedin_link = models.URLField(null=True, blank=True)
    Instagram_link = models.URLField(null=True, blank=True)
    Phone_number = models.CharField(max_length=15, null=False, blank=False)


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_type = models.CharField(max_length=20)
    skill_name = models.CharField(max_length=50)
