# Generated by Django 4.2.9 on 2024-07-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_language_education_resume_educations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='certificate_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
