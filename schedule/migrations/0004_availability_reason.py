# Generated by Django 2.2.5 on 2021-06-16 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_availability_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='reason',
            field=models.TextField(blank=True),
        ),
    ]
