# Generated by Django 4.2.7 on 2023-11-04 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0006_alter_appuser_killer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='killer',
        ),
    ]