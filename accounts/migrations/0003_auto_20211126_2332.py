# Generated by Django 2.2 on 2021-11-27 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211126_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regi',
            name='password1',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='regi',
            name='password2',
            field=models.CharField(max_length=12),
        ),
    ]
