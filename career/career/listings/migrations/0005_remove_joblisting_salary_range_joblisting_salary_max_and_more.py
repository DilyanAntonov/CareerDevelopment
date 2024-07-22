# Generated by Django 4.2.9 on 2024-07-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_joblisting_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblisting',
            name='salary_range',
        ),
        migrations.AddField(
            model_name='joblisting',
            name='salary_max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='joblisting',
            name='salary_min',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='employment_type',
            field=models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time'), ('CT', 'Contract'), ('TP', 'Temporary'), ('IN', 'Intern')], default='FT', max_length=2),
        ),
    ]