# Generated by Django 3.2.3 on 2021-08-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210812_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='imagen',
        ),
        migrations.AddField(
            model_name='skill',
            name='imagen',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]
