# Generated by Django 4.2.9 on 2024-08-16 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblisting',
            name='application_deadline',
        ),
    ]
