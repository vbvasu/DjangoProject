from django.contrib import admin

from .models import UserProfile, Skill, Project, Education
admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)


# Register your models here.
