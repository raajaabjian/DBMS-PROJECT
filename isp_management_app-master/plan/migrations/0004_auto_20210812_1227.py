# Generated by Django 3.2.6 on 2021-08-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]