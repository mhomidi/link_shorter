# Generated by Django 3.0.3 on 2020-02-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20200215_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='browser',
            field=models.IntegerField(choices=[(0, 'Chrome'), (1, 'Mozila'), (2, 'SAFARI'), (3, 'IE'), (4, 'Opera')], default=0, verbose_name='Browser'),
        ),
    ]
