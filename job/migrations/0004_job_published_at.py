# Generated by Django 3.1.5 on 2021-01-13 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateField(auto_now=True),
        ),
    ]
