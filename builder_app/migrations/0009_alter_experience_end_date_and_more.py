# Generated by Django 4.2.3 on 2023-07-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder_app', '0008_remove_education_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
