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
    Skill_no = models.IntegerField(blank=False, default=0)
    Certification_no = models.IntegerField(blank=False,default=0)
    Cofee_no = models.IntegerField(blank=False,default=0)
    Resume = models.FileField(null=True, blank=True, upload_to='resumes/')
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_pictures/')
    logo_picture = models.ImageField(null=True, blank=True, upload_to='logo_pictures/')
    background_picture = models.ImageField(null=True, blank=True, upload_to='background_pictures/')


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_type = models.CharField(max_length=20)
    skill_name = models.CharField(max_length=50)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_category = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50)
    project_description = models.TextField(max_length=1000, null=False, blank=False)
    project_picture = models.ImageField(upload_to='project_pictures/', null=True, blank=True)
    project_link = models.URLField(max_length=200)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    highest_edu = models.CharField(max_length=10, null=True, blank=True)
    pg_field = models.CharField(max_length=50, null=True, blank=True)
    pg_univ = models.CharField(max_length=50, null=True, blank=True)
    pg_city = models.CharField(max_length=50, null=True, blank=True)
    pg_year = models.IntegerField(null=True, blank=True)
    pg_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ug_field = models.CharField(max_length=50, null=True, blank=True)
    ug_univ = models.CharField(max_length=50, null=True, blank=True)
    ug_city = models.CharField(max_length=50, null=True, blank=True)
    ug_year = models.IntegerField(null=True, blank=True)
    ug_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tlv_field = models.CharField(max_length=50, null=True, blank=True)
    tlv_univ = models.CharField(max_length=50, null=True, blank=True)
    tlv_city = models.CharField(max_length=50, null=True, blank=True)
    tlv_year = models.IntegerField(null=True, blank=True)
    tlv_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ten_univ = models.CharField(max_length=50, null=True, blank=True)
    ten_city = models.CharField(max_length=50, null=True, blank=True)
    ten_year = models.IntegerField(null=True, blank=True)
    ten_percent = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

