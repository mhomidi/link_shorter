# Generated by Django 3.0.3 on 2020-02-14 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('short_url', '0002_auto_20200214_1342'),
        ('analytics', '0003_auto_20200214_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observation',
            name='last_30_days',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='last_date_click',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='short_url',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='today_click',
        ),
        migrations.AddField(
            model_name='observation',
            name='browser',
            field=models.IntegerField(choices=[('Chrome', 0), ('Mozila', 1), ('SAFARI', 2), ('IE', 3), ('Opera', 4)], default=0, verbose_name='Browser'),
        ),
        migrations.AddField(
            model_name='observation',
            name='device',
            field=models.IntegerField(choices=[('Mobile', 0), ('Desktop', 1)], default=0, verbose_name='Device'),
        ),
        migrations.AddField(
            model_name='urlobservation',
            name='short_url',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='short_url.ShortURL'),
        ),
        migrations.AddField(
            model_name='userobservation',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userobservation',
            name='short_url',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='short_url.ShortURL'),
        ),
    ]
