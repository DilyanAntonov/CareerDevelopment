# Generated by Django 4.2.9 on 2024-08-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobTrend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programming_language', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('number_of_jobs', models.IntegerField()),
            ],
        ),
    ]
