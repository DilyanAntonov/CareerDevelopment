# Generated by Django 4.2.9 on 2024-08-04 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resume', '0001_initial'),
        ('application', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resume.resume'),
        ),
    ]
