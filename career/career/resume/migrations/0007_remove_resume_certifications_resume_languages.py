# Generated by Django 4.2.9 on 2024-07-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_alter_education_certificate_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='certifications',
        ),
        migrations.AddField(
            model_name='resume',
            name='languages',
            field=models.ManyToManyField(blank=True, to='resume.language'),
        ),
    ]
