# Generated by Django 4.2.9 on 2024-08-04 16:23

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('employees_num', models.IntegerField(blank=True, null=True)),
                ('industry', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=200)),
                ('contact_email', models.EmailField(max_length=254)),
                ('logo', models.ImageField(blank=True, upload_to='company_logos/')),
                ('established_year', models.IntegerField(blank=True, null=True)),
                ('eik', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.baseuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
