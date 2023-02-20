# Generated by Django 4.1.5 on 2023-02-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_project_userprofile_certification_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background_picture',
            field=models.ImageField(blank=True, null=True, upload_to='background_pictures/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='logo_picture',
            field=models.ImageField(blank=True, null=True, upload_to='logo_pictures/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]