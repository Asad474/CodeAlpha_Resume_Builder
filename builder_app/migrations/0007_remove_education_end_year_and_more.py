# Generated by Django 4.2.3 on 2023-07-24 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder_app', '0006_userprofile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='end_year',
        ),
        migrations.RemoveField(
            model_name='education',
            name='start_year',
        ),
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='education',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
