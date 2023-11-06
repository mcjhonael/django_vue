# Generated by Django 3.2.3 on 2021-08-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210807_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='persona/avatar'),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='post/imagen'),
        ),
    ]
