# Generated by Django 3.1.5 on 2021-01-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patriot_cadapp', '0002_auto_20210130_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='insurance',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='registration',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
