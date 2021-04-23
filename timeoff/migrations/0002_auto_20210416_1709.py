# Generated by Django 2.2.5 on 2021-04-16 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timeoff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeoff',
            old_name='text_box',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='timeoff',
            old_name='requested_timeoff',
            new_name='from_date',
        ),
        migrations.RenameField(
            model_name='timeoff',
            old_name='username',
            new_name='user',
        ),
        migrations.AddField(
            model_name='timeoff',
            name='approved_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeoff',
            name='status',
            field=models.CharField(default=None, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeoff',
            name='to_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timeoff',
            name='submission_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]