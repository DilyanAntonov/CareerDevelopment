# Generated by Django 4.2.9 on 2024-08-04 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0001_initial'),
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='job_listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.joblisting'),
        ),
    ]
