# Generated by Django 2.2.5 on 2021-06-16 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20210616_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]