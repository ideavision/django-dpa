# Generated by Django 2.2.6 on 2021-03-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='plotlydashapp',
            name='dash_orginal_name',
            field=models.CharField(default='test name', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plotlydashapp',
            name='title',
            field=models.CharField(default='test title', max_length=200),
            preserve_default=False,
        ),
    ]
