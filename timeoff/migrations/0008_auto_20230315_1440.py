# Generated by Django 2.2.5 on 2023-03-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeoff', '0007_auto_20230315_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeoff',
            name='end_date',
            field=models.DateField(blank=True, default='2000-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='timeoff',
            name='start_date',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
